<script>
  import "carbon-components-svelte/css/white.css";
  import { _ } from "svelte-i18n";
  import { fly } from "svelte/transition";
  import { Button } from "carbon-components-svelte";
  import ChevronRight from "carbon-icons-svelte/lib/ChevronRight.svelte";
  import PageWelcome from "./PageWelcome.svelte";
  import PageConsent from "./PageConsent.svelte";
  import PageQ1 from "./PageQ1.svelte";

  // Initialize internationalization
  import "./i18n.js";

  // CONSTANTS
  let progress_values = { PageWelcome: 0, PageConsent: 25, PageQ1: 50 };

  // STATES

  // Current Page
  let main_state = "PageQ1";
  // Bottom bar states
  let bottom_bar_next_enabled = true;
  // Student sciper ID (given by user)
  let sciperID = undefined;
  // Course ID (given by user)
  let courseID = undefined;
  // Course & Task names (gathered from server)
  let course_name = undefined;
  let task_name = undefined;
  // Task & Answer Body (gathered from server)
  let task_body = undefined;
  let answer_body = undefined;
  // Feedbacks (gathered from server)
  let feedback_AI_body = undefined;
  let feedback_human_body = undefined;

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
      main_state = "PageQ1";
    }
  }

  // Gather all necessary student data from server
  async function gather_data() {
    // Wait 1 sec
    await new Promise((resolve) => setTimeout(resolve, 1000));
    // Course & Task names (gathered from server)
    course_name = "DummyCourseName";
    task_name = "DummyTaskName";
    // Task & Answer Body (gathered from server)
    task_body =
      "This is a dummy task body in markdown. This is an equation $x^2 = y$";
    answer_body =
      "This is a dummy answer body in markdown with another equation $x*y=0$";
    // Feedbacks (gathered from server)
    feedback_AI_body = "Dummy AI feedback. $x+y=z$";
    feedback_human_body = "Dummy Human feedback. $i+2j$";
  }
  // TMP to remove
  function gather_data_dummy() {
    // Course & Task names (gathered from server)
    course_name = "DummyCourseName";
    task_name = "DummyTaskName";
    // Task & Answer Body (gathered from server)
    task_body =
      "This is a dummy task body in markdown. This is an equation $x^2 = y$";
    answer_body =
      "This is a dummy answer body in markdown with another equation $x*y=0$";
    // Feedbacks (gathered from server)
    feedback_AI_body = "Dummy AI feedback. $x+y=z$";
    feedback_human_body = "Dummy Human feedback. $i+2j$";
  }
  gather_data_dummy();
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
          />
        {:else}
          Error : unkown main_state
        {/if}
      </div>
    {/key}

    <div id="bottom_bar">
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

    <div style="width: {progress}%;" id="progress_bar" />
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

  @media (min-width: 1024px) {
    #main_container {
      width: 1024px;
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
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
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
</style>
