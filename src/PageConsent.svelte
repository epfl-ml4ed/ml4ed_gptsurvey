<script>
    import { _ } from "svelte-i18n";
    import { Checkbox } from "carbon-components-svelte";
    import { TextInput } from "carbon-components-svelte";
    import { Dropdown } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let courseID;
    export let course_name;

    sciperID = "";

    let selected_courseID = null;
    let selected_taskID = null;
    let agree_and_over18 = false;
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
        // {
        //     id: "CS-119(g)",
        //     text: "CS-119(g): Information, calcul, communication (SV)",
        // },
        {
            id: "CS-119(h)",
            text: "CS-119(h): Information, calcul, communication (GC)",
        },
        { id: "CS-401", text: "CS-401: Applied data analysis" },
        // {
        //     id: "CS-431",
        //     text: "CS-431: Introduction to natural language processing",
        // },
        // { id: "CS-433", text: "CS-433: Machine learning" },
        // { id: "CS-502", text: "CS-502: Deep learning in biomedicine" },
        { id: "MATH-101(c)", text: "MATH-101(c): Analysis I", tasks: ["Exercice14", "Exercice15"] },
        { id: "MATH-101(ol)", text: "MATH-101(ol): Analyse I (online)", tasks: ["Exercice14", "Exercice15"] },
    ];

    $: task_required = courses_items.filter((c) => c.id === selected_courseID)[0].tasks !== undefined;
    $: tasks_items = courses_items.filter((c) => c.id === selected_courseID)[0].tasks?.map((t) => ({ id: t, text: t })).concat([{ id: null, text: " " }]);
    $: course_name = courses_items.filter((c) => c.id === selected_courseID)[0].text;
    $: courseID = (task_required) ? selected_courseID + "---" + selected_taskID : selected_courseID;
    $: task_valid = (selected_taskID && task_required) || !task_required;
    $: sciperID_range_invalid =
        sciperID.length != 6 ||
        ![...sciperID].every((c) => "0123456789".includes(c));
    $: bottom_bar_next_enabled = agree_and_over18 && !sciperID_range_invalid && courseID && task_valid;
</script>

<h1 id="title">{$_("pageconsent_title")}</h1>
<div class="declaration_block">
    <p style="margin-bottom">{$_("pageconsent_text")}</p>
</div>
<br />
<div
    style="border: 1px solid rgb(242, 242, 242); margin-bottom:8px; margin-top:8px"
/>
<Checkbox
    bind:checked={agree_and_over18}
    id="agree"
    labelText={$_("pageconsent_checkbox_agree_and_over18")}
/>
<div
    style="border: 1px solid rgb(242, 242, 242); margin-bottom:8px; margin-top:8px"
/>
<br />
<p>{$_("pageconsent_sciper")}</p>
<br />
<TextInput
    labelText="SCIPER"
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
    items={courses_items}
    bind:selectedId={selected_courseID}
    invalidText={$_("pageconsent_course_invalid")}
    invalid={courseID == null}
/>

{#if task_required}
<br />
    <p>{$_("pageconsent_task")}</p>
    <br />
    <Dropdown
        direction="top"
        titleText="TASK"
        items={tasks_items}
        bind:selectedId={selected_taskID}
        invalidText={$_("pageconsent_task_invalid")}
        invalid={!task_valid}
    />
{/if}

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
