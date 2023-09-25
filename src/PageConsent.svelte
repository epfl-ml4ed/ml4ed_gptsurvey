<script>
    import { _ } from "svelte-i18n";
    import { Checkbox } from "carbon-components-svelte";
    import { NumberInput } from "carbon-components-svelte";
    import { Dropdown } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let courseID;

    let agree = false;
    let over18 = false;
    let sciperID_range_invalid = true;
    $: sciperID_range_invalid =
        !sciperID || sciperID < 100000 || sciperID > 999999;
    $: bottom_bar_next_enabled = agree && over18 && !sciperID_range_invalid;
</script>

<h1 id="title">{$_("pageconsent_title")}</h1>
<div class="declaration_block">
    <p style="margin-bottom">{$_("pageconsent_text")}</p>
</div>
<br />
<Checkbox
    bind:checked={agree}
    id="agree"
    labelText={$_("pageconsent_checkbox_agree")}
/>
<br />
<Checkbox
    bind:checked={over18}
    id="over18"
    labelText={$_("pageconsent_checkbox_over18")}
/>
<br />
<p>{$_("pageconsent_sciper")}</p>
<br />
<NumberInput
    hideSteppers
    label="SCIPER"
    bind:value={sciperID}
    bind:invalid={sciperID_range_invalid}
    invalidText={$_("pageconsent_sciper_invalid")}
/>
<br />
<p>{$_("pageconsent_course")}</p>
<br />
<Dropdown
    direction="top"
    titleText="COURSE"
    placeholder="Select contact method"
    items={[
        { id: null, text: " " },
        { id: "CourseA_ID", text: "CourseA" },
        { id: "CourseB_ID", text: "CourseB" },
        { id: "CourseC_ID", text: "CourseC" },
    ]}
    bind:selectedId={courseID}
    invalidText={$_("pageconsent_course_invalid")}
    invalid={courseID == null}
/>

<style>
    #title {
        margin-top: 0px;
        margin-bottom: 32px;
        text-align: center;
    }

    p {
        white-space: pre-line;
        text-align: justify;
    }

    :global(.bx--content-switcher__label) {
        white-space: normal !important;
        text-align: center !important;
        width: inherit !important;
    }

    .declaration_block {
        background-color: #efefef73;
        overflow-y: scroll;
        padding-top: 16px;
        padding-bottom: 16px;
        border: solid 1px #e6e6e6;
        border-radius: 8px;
        padding: 16px;
    }
</style>
