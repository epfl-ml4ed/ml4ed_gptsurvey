<script>
  import "carbon-components-svelte/css/white.css";
  import { _ } from "svelte-i18n";
  import { fly, fade } from "svelte/transition";
  import { Button } from "carbon-components-svelte";
  import ChevronRight from "carbon-icons-svelte/lib/ChevronRight.svelte";
  import PageWelcome from "./PageWelcome.svelte";
  import PageConsent from "./PageConsent.svelte";
  import PageQ1 from "./PageQ1.svelte";
  import PageQ2 from "./PageQ2.svelte";
  import PageQ3 from "./PageQ3.svelte";
  import PageQ4 from "./PageQ4.svelte";
  import PageThanks from "./PageThanks.svelte";
  import PageAdmin from "./PageAdmin.svelte";

  // Initialize internationalization
  import "./i18n.js";

  // CONSTANTS
  let progress_values = {
    PageWelcome: 0,
    PageConsent: 10,
    PageQ1: 20,
    PageQ2: 40,
    PageQ3: 60,
    PageQ4: 80,
    PageThanks: 100,
  };

  // STATES

  // Current Page
  let main_state = "PageWelcome";
  // Bottom bar states
  let bottom_bar_next_enabled = true;
  // Loading popup
  let loading_popup_msg = "";
  // Student sciper ID (given by user)
  let sciperID = null;
  // Course ID (given by user)
  let courseID = null;
  // Course & Task names (gathered from server)
  let course_name = null;
  let task_name = null;
  // Task & Answer Body (gathered from server)
  let task_body = null;
  let answer_body = null;
  // Feedbacks (gathered from server)
  let feedback_AI_body = null;
  let feedback_human_body = null;
  // Student likert answers on page Q1 (given by user)
  let Q1_likert_AI = null;
  let Q1_likert_human = null;
  // Student answers on page Q2 (given by user)
  let Q2_selected_feedback = null;
  let Q2_explain_txt = null;
  // Student likert answers on page Q3 (given by user)
  // Initially same as Q1, then overwritten on page Q3
  let Q3_likert_AI = null;
  let Q3_likert_human = null;
  // Student extra likert answers on page Q3 (given by user)
  let Q3_extra_likert_AI = null;
  let Q3_extra_likert_human = null;
  // Student background / demographics (given by user)
  let Q4_student_age = null;
  let Q4_student_edtech = null;
  let Q4_student_gender = null;
  let Q4_student_section = null;

  // DERIVED STATES

  $: bottom_bar_message = bottom_bar_next_enabled
    ? $_("common_pressnext")
    : $_("common_fillall");

  // Progress var value (in %)
  $: progress = progress_values[main_state];

  // FUNCTIONS

  async function next_func() {
    if (main_state == "PageWelcome") {
      main_state = "PageConsent";
    } else if (main_state == "PageConsent") {
      await gather_data();
    } else if (main_state == "PageQ1") {
      main_state = "PageQ2";
    } else if (main_state == "PageQ2") {
      Q3_likert_AI = structuredClone(Q1_likert_AI);
      Q3_likert_human = structuredClone(Q1_likert_human);
      main_state = "PageQ3";
    } else if (main_state == "PageQ3") {
      main_state = "PageQ4";
    } else if (main_state == "PageQ4") {
      await send_results();
    }
  }

  // Gather all necessary student data from server
  async function gather_data() {
    loading_popup_msg = $_("common_loading");
    try {
      const response = await fetch(
        `${
          import.meta.env.VITE_BACKEND
        }gather_data?sciperID=${sciperID}&courseID=${courseID}`
      );
      let resp_j = await response.json();
      if (!response.ok) {
        loading_popup_msg = `Error : ${resp_j.detail}`;
      } else {
        task_name = resp_j["TaskName"];
        task_body = resp_j["TaskBody"];
        answer_body = resp_j["TaskSolutionBody"];
        feedback_AI_body = resp_j["AIFeedback"];
        feedback_human_body = resp_j["HumanFeedback"];
        // Go to next page
        main_state = "PageQ1";
        loading_popup_msg = "";
      }
    } catch (error) {
      loading_popup_msg = `Error : Server Unreachable (${error})`;
    }
    // Wait 3secs and close popup
    await new Promise((resolve) => setTimeout(resolve, 3000));
    loading_popup_msg = "";
  }

  // Send results to server
  async function send_results() {
    let results = {
      SciperID: sciperID,
      CourseID: courseID,
      task_name: task_name,
      results: {
        Q1_likert_AI: Q1_likert_AI,
        Q1_likert_human: Q1_likert_human,
        Q2_selected_feedback: Q2_selected_feedback,
        Q2_explain_txt: Q2_explain_txt,
        Q3_likert_AI: Q3_likert_AI,
        Q3_likert_human: Q3_likert_human,
        Q3_extra_likert_AI: Q3_extra_likert_AI,
        Q3_extra_likert_human: Q3_extra_likert_human,
        Q4_student_age: Q4_student_age,
        Q4_student_edtech: Q4_student_edtech,
        Q4_student_gender: Q4_student_gender,
        Q4_student_section: Q4_student_section,
      },
    };
    loading_popup_msg = $_("common_loading");
    try {
      const response = await fetch(
        `${import.meta.env.VITE_BACKEND}write_results`,
        {
          method: "POST",
          body: JSON.stringify(results),
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
        }
      );
      let resp_j = await response.json();
      if (!response.ok) {
        loading_popup_msg = `Error : ${resp_j.detail}`;
      } else {
        // Go to next page
        main_state = "PageThanks";
        loading_popup_msg = "";
      }
    } catch (error) {
      loading_popup_msg = `Error : Server Unreachable, 
      make sure your connection is working and try again. 
      Otherwise contact support. (${error})`;
    }
    // Wait 3secs and close popup
    await new Promise((resolve) => setTimeout(resolve, 3000));
    loading_popup_msg = "";
  }

  // In production always start at PageWelcome, ask before quit
  if (import.meta.env.MODE == "production") {
    main_state = "PageWelcome";
    window.onbeforeunload = (e) => "Are you sure you want to quit ?";
  }

  // On last page disable quit popup
  $: if (main_state == "PageThanks" || main_state == "PageAdmin") {
    window.onbeforeunload = null;
  }

  // Special URL for admin page to upload csv data
  if (window.location.href.split("?")[1] == "courses_upload_csv_data") {
    main_state = "PageAdmin";
  }

  // In dev mode, pre-fill states with dummy data
  if (import.meta.env.MODE == "development") {
    main_state = "PageWelcome";
    course_name = "DummyCourseName";
    task_name = "DummyTaskName";
    task_body =
      "This is a dummy task body in markdown. $$\\left( \\sum_{k=1}^n a_k b_k \\right)^2 \\leq \\left( \\sum_{k=1}^n a_k^2 \\right) \\left( \\sum_{k=1}^n b_k^2 \\right)$$";
    answer_body =
      "This is a dummy answer body in markdown with another equation $x*y=0$";
    feedback_AI_body = "Dummy AI feedback. $x+y=z$";
    feedback_human_body = "Dummy Human feedback. $i+2j$";
  }
</script>

<main>
  <div id="main_container">
    {#key main_state}
      <div
        id="page_container"
        in:fly={{ x: 400, y: 0, duration: 600 }}
        out:fly={{ x: -600, y: 0, duration: 400 }}
      >
        {#if main_state == "PageWelcome"}
          <PageWelcome />
        {:else if main_state == "PageConsent"}
          <PageConsent
            bind:bottom_bar_next_enabled
            bind:sciperID
            bind:courseID
            bind:course_name
          />
        {:else if main_state == "PageQ1"}
          <PageQ1
            bind:bottom_bar_next_enabled
            {sciperID}
            {course_name}
            {task_name}
            {task_body}
            {answer_body}
            {feedback_AI_body}
            {feedback_human_body}
            bind:likert_AI={Q1_likert_AI}
            bind:likert_human={Q1_likert_human}
          />
        {:else if main_state == "PageQ2"}
          <PageQ2
            bind:bottom_bar_next_enabled
            {sciperID}
            bind:selected_feedback={Q2_selected_feedback}
            bind:explain_txt={Q2_explain_txt}
            {feedback_AI_body}
            {feedback_human_body}
          />
        {:else if main_state == "PageQ3"}
          <PageQ3
            bind:bottom_bar_next_enabled
            {sciperID}
            {feedback_AI_body}
            {feedback_human_body}
            bind:likert_AI={Q3_likert_AI}
            bind:likert_human={Q3_likert_human}
            bind:extra_likert_AI={Q3_extra_likert_AI}
            bind:extra_likert_human={Q3_extra_likert_human}
          />
        {:else if main_state == "PageQ4"}
          <PageQ4
            bind:bottom_bar_next_enabled
            bind:student_age={Q4_student_age}
            bind:student_edtech={Q4_student_edtech}
            bind:student_gender={Q4_student_gender}
            bind:student_section={Q4_student_section}
          />
        {:else if main_state == "PageThanks"}
          <PageThanks />
        {:else if main_state == "PageAdmin"}
          <PageAdmin />
        {:else}
          Error : unkown main_state
        {/if}
      </div>
    {/key}
    {#if main_state != "PageThanks" && main_state != "PageAdmin"}
      <div
        id="bottom_bar"
        in:fly={{ y: -80, x: 0, duration: 600 }}
        out:fly={{ y: 80, x: 0, duration: 600 }}
      >
        <p
          style="color: {bottom_bar_next_enabled ? 'black' : '#a60606'}"
          id="next_text"
        >
          {bottom_bar_message}
        </p>
        <Button
          disabled={!bottom_bar_next_enabled}
          icon={ChevronRight}
          on:click={next_func}>{$_("common_next")}</Button
        >
      </div>
    {/if}
    <div style="width: {progress}%;" id="progress_bar" />
    {#if loading_popup_msg !== ""}
      <div id="loading_popup" transition:fade>
        <h3>{loading_popup_msg}</h3>
      </div>
    {/if}
  </div>
</main>

<style>
  #main_container {
    background-color: white;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 0;
    margin-bottom: 0;
    overflow: hidden;
  }

  #page_container {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    overflow: scroll;
    padding: 16px;
    padding-bottom: 66px;
  }

  @media (min-width: 1200px) {
    #main_container {
      width: 1200px;
      margin-top: 32px;
      margin-bottom: 32px;
      border-radius: 8px;
      border: solid 1px #dbdbdb;
    }
    #page_container {
      padding-top: 64px;
      padding-bottom: 64px;
      padding-right: 128px;
      padding-left: 128px;
    }
  }

  #progress_bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background-color: #0f62fe;
    transition: all 1s;
  }

  #bottom_bar {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #efefef73;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: start;
    flex-wrap: nowrap;
    border-top: solid 1px #e6e6e6;
    backdrop-filter: blur(8px);
  }

  #next_text {
    width: 100%;
    margin-left: 16px;
    margin-right: 16px;
    opacity: 50%;
    text-align: center;
  }

  #loading_popup {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #efefef9b;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-wrap: nowrap;
    backdrop-filter: blur(8px);
    padding: 16px;
  }
</style>
