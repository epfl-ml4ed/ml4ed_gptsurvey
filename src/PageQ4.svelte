<script>
    import { _ } from "svelte-i18n";
    import { NumberInput } from "carbon-components-svelte";
    import { Dropdown } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;

    export let student_age = null;
    export let student_edtech = null;
    export let student_gender = null;
    export let student_section = null;

    $: bottom_bar_next_enabled =
        student_age != null &&
        student_edtech != null &&
        student_gender != null &&
        student_section != null;

    let gender_items = [
        { id: null, text: " " },
        { id: "female", text: $_("pageq4_gender_female") },
        { id: "male", text: $_("pageq4_gender_male") },
        { id: "nonbinary", text: $_("pageq4_gender_nonbinary") },
        { id: "notsay", text: $_("pageq4_gender_notsay") },
    ];

    let section_items = [
        { id: null, text: " " },
        {
            id: "BA - Chemistry and Chemical Engineering",
            text: "BA - Chemistry and Chemical Engineering",
        },
        { id: "BA - Mathematics", text: "BA - Mathematics" },
        { id: "BA - Physics", text: "BA - Physics" },
        { id: "BA - Computer Science", text: "BA - Computer Science" },
        {
            id: "BA - Communication Systems",
            text: "BA - Communication Systems",
        },
        {
            id: "BA - Electrical and Electronic Engineering",
            text: "BA - Electrical and Electronic Engineering",
        },
        {
            id: "BA - Mechanical Engineering",
            text: "BA - Mechanical Engineering",
        },
        {
            id: "BA - Microengineering",
            text: "BA - Microengineering",
        },
        {
            id: "BA - Materials Science and Engineering",
            text: "BA - Materials Science and Engineering",
        },
        {
            id: "BA - Life Sciences Engineering",
            text: "BA - Life Sciences Engineering",
        },
        {
            id: "BA - Architecture",
            text: "BA - Architecture",
        },
        {
            id: "BA - Civil Engineering",
            text: "BA - Civil Engineering",
        },
        {
            id: "BA - Environmental Sciences and Engineering",
            text: "BA - Environmental Sciences and Engineering",
        },
        {
            id: "MA - Architecture",
            text: "MA - Architecture",
        },
        {
            id: "MA - Civil Engineering",
            text: "MA - Civil Engineering",
        },
        {
            id: "MA - Environmental Sciences and Engineering",
            text: "MA - Environmental Sciences and Engineering",
        },
        {
            id: "MA - Electrical and Electronic Engineering",
            text: "MA - Electrical and Electronic Engineering",
        },
        {
            id: "MA - Mechanical Engineering",
            text: "MA - Mechanical Engineering",
        },
        {
            id: "MA - Microengineering",
            text: "MA - Microengineering",
        },
        {
            id: "MA - Robotics",
            text: "MA - Robotics",
        },
        {
            id: "MA - Materials Science and Engineering",
            text: "MA - Materials Science and Engineering",
        },
        {
            id: "MA - Energy Science and Technology",
            text: "MA - Energy Science and Technology",
        },
        {
            id: "MA - Computer Science",
            text: "MA - Computer Science",
        },
        {
            id: "MA - Communication Systems",
            text: "MA - Communication Systems",
        },
        {
            id: "MA - Data Science",
            text: "MA - Data Science",
        },
        {
            id: "MA - Cyber Security",
            text: "MA - Cyber Security",
        },
        {
            id: "MA - Molecular and Biological Chemistry",
            text: "MA - Molecular and Biological Chemistry",
        },
        {
            id: "MA - Chemical Engineering and Biotechnology",
            text: "MA - Chemical Engineering and Biotechnology",
        },
        {
            id: "MA - Mathematics",
            text: "MA - Mathematics",
        },
        {
            id: "MA - Applied Mathematics",
            text: "MA - Applied Mathematics",
        },
        {
            id: "MA - Statistics",
            text: "MA - Statistics",
        },
        {
            id: "MA - Computational Science and Engineering",
            text: "MA - Computational Science and Engineering",
        },
        {
            id: "MA - Physics",
            text: "MA - Physics",
        },
        {
            id: "MA - Applied Physics",
            text: "MA - Applied Physics",
        },
        {
            id: "MA - Nuclear Engineering",
            text: "MA - Nuclear Engineering",
        },
        {
            id: "MA - Life Sciences Engineering",
            text: "MA - Life Sciences Engineering",
        },
        {
            id: "MA - Financial Engineering",
            text: "MA - Financial Engineering",
        },
        {
            id: "MA - Management, Technology and Entrepreneurship",
            text: "MA - Management, Technology and Entrepreneurship",
        },
        {
            id: "MA - Sustainable Management and Technology",
            text: "MA - Sustainable Management and Technology",
        },
        {
            id: "MA - Digital Humanities",
            text: "MA - Digital Humanities",
        },
        {
            id: "MA - Neuro-X",
            text: "MA - Neuro-X",
        },
        {
            id: "MA - Quantum Science and Engineering",
        },
        { id: "Other", text: "Other" },
    ];
</script>

<h1 id="title">{$_("pageq4_title")}</h1>
<p>{$_("pageq4_txt1")}</p>
<br />
<NumberInput
    allowEmpty
    bind:value={student_age}
    label={$_("pageq4_age")}
    min={18}
    max={99}
    invalid={student_age == null}
/>
<br />
<br />
<NumberInput
    allowEmpty
    bind:value={student_edtech}
    label={$_("pageq4_edtech")}
    min={0}
    max={99}
    invalid={student_edtech == null}
/>
<br />
<br />
<Dropdown
    titleText={$_("pageq4_gender")}
    bind:selectedId={student_gender}
    items={gender_items}
    invalid={student_gender == null}
    direction="top"
/>
<br />
<br />
<Dropdown
    titleText={$_("pageq4_section")}
    bind:selectedId={student_section}
    items={section_items}
    invalid={student_section == null}
    direction="top"
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
</style>
