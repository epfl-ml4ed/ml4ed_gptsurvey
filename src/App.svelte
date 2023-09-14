<script>
  import "carbon-components-svelte/css/white.css";
  import { _ } from "svelte-i18n";
  import { fly } from "svelte/transition";
  import { Button } from "carbon-components-svelte";
  import ChevronRight from "carbon-icons-svelte/lib/ChevronRight.svelte";
  import PageWelcome from "./PageWelcome.svelte";
  import PageConsent from "./PageConsent.svelte";

  // Initialize internationalization
  import "./i18n.js";

  // STATES

  // Current Page
  let main_state = "PageConsent";
  // Progress var value (in %)
  let progress = 0;
  // Bottom bar states
  let bottom_bar_next_enabled = true;

  // DERIVED STATES

  $: bottom_bar_message = bottom_bar_next_enabled
    ? $_("common_pressnext")
    : $_("common_fillall");

  // FUNCTIONS

  function next_func() {
    main_state = "PageConsent";
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
          <PageConsent bind:bottom_bar_next_enabled />
        {:else}
          Error : unkown main_state
        {/if}
      </div>
    {/key}
    <div style="width: {progress}%;" id="progress_bar" />

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

  @media (min-width: 780px) {
    #main_container {
      width: 720px;
      margin-top: 32px;
      margin-bottom: 32px;
      border-radius: 8px;
      border: solid 1px #e6e6e6;
    }
    #page_container {
      padding: 64px;
    }
  }

  #progress_bar {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: red;
    transition: all 1s;
  }

  #bottom_bar {
    z-index: 4;
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
