<script>
    import { _ } from "svelte-i18n";
    import { Checkbox } from "carbon-components-svelte";
    import { TextInput } from "carbon-components-svelte";
    import { Dropdown } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let courseID;
    export let course_name;

    let agree = false;
    let over18 = false;
    let sciperID_range_invalid = true;

    let courses_items = [
        { id: null, text: " " },
        {
            id: "BIO-210",
            text: "BIO-210: Applied software engineering for life sciences",
        },
        {
            id: "CS-101",
            text: "CS-101: Advanced information, computation, communication I",
        },
        {
            id: "CS-119(d)",
            text: "CS-119(d): Information, calcul, communication (Math)",
        },
        {
            id: "CS-119(g)",
            text: "CS-119(g): Information, calcul, communication (SV)",
        },
        {
            id: "CS-119(h)",
            text: "CS-119(h): Information, calcul, communication (GC)",
        },
        { id: "CS-401", text: "CS-401: Applied data analysis" },
        {
            id: "CS-431",
            text: "CS-431: Introduction to natural language processing",
        },
        { id: "CS-433", text: "CS-433: Machine learning" },
        { id: "CS-502", text: "CS-502: Deep learning in biomedicine" },
        { id: "MATH-101(c)", text: "MATH-101(c): Analysis I" },
        { id: "MATH-101(ol)", text: "MATH-101(ol): Analyse I (online)" },
    ];

    sciperID = "";
    $: course_name = courses_items.filter((c) => c.id == courseID)[0].text;
    $: sciperID_range_invalid =
        sciperID.length != 6 ||
        ![...sciperID].every((c) => "0123456789".includes(c));
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
<TextInput
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
    items={courses_items}
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
