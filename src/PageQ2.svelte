<script>
    import { _ } from "svelte-i18n";
    import { RadioButtonGroup, RadioButton } from "carbon-components-svelte";
    import { TextArea } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let selected_feedback;
    export let explain_txt;

    let selected_blind_feedback = undefined;

    explain_txt = "";

    $: bottom_bar_next_enabled =
        selected_blind_feedback !== undefined && explain_txt !== "";

    // Convert from feedback 1/2 to real feedback AI/human
    let random_layout_state = sciperID % 2;
    $: if (random_layout_state == 0) {
        if (selected_blind_feedback == "feedback1") {
            selected_feedback = "feedback_AI";
        } else if (selected_blind_feedback == "feedback2") {
            selected_feedback = "feedback_human";
        } else {
            selected_feedback = undefined;
        }
    } else {
        if (selected_blind_feedback == "feedback1") {
            selected_feedback = "feedback_human";
        } else if (selected_blind_feedback == "feedback2") {
            selected_feedback = "feedback_AI";
        } else {
            selected_feedback = undefined;
        }
    }
</script>

<h1 id="title">{$_("pageq2_title")}</h1>
<p>{$_("pageq2_txt1")}</p>
<p id="block">{$_("pageq2_txt2")}</p>
<p>{$_("pageq2_txt3")}</p>
<br />
<RadioButtonGroup
    name="radio-button-group"
    bind:selected={selected_blind_feedback}
>
    <RadioButton value="feedback1" id="feedback1" labelText={$_("pageq2_a1")} />
    <RadioButton value="feedback2" id="feedback2" labelText={$_("pageq2_a2")} />
</RadioButtonGroup>
<br />
<p>{$_("pageq2_txt4")}</p>
<br />
<TextArea
    bind:value={explain_txt}
    invalid={explain_txt == ""}
    invalidText={$_("pageq2_invalid")}
    placeholder={$_("pageq2_txt5")}
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

    #block {
        font-weight: 600;
        background-color: #ffe6d9;
        border: 1px solid #e5bca8;
        border-radius: 8px;
        margin-top: 16px;
        margin-bottom: 16px;
        padding: 16px;
    }
</style>
