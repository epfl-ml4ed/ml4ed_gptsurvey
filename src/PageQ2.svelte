<script>
    import { _ } from "svelte-i18n";
    import { RadioButtonGroup, RadioButton } from "carbon-components-svelte";
    import { TextArea } from "carbon-components-svelte";
    import { Carta, CartaViewer } from "carta-md";
    import { math } from "@cartamd/plugin-math";

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let selected_feedback;
    export let explain_txt;
    export let feedback_AI_body;
    export let feedback_human_body;

    const carta = new Carta({
        extensions: [math()],
    });

    let selected_blind_feedback = null;

    explain_txt = "";

    $: bottom_bar_next_enabled =
        selected_blind_feedback !== null && explain_txt !== "";

    // Convert from feedback 1/2 to real feedback AI/human
    let random_layout_state = sciperID % 2;
    $: if (random_layout_state == 0) {
        if (selected_blind_feedback == "feedback1") {
            selected_feedback = "feedback_AI";
        } else if (selected_blind_feedback == "feedback2") {
            selected_feedback = "feedback_human";
        } else {
            selected_feedback = null;
        }
    } else {
        if (selected_blind_feedback == "feedback1") {
            selected_feedback = "feedback_human";
        } else if (selected_blind_feedback == "feedback2") {
            selected_feedback = "feedback_AI";
        } else {
            selected_feedback = null;
        }
    }
</script>

<h1 id="title">{$_("pageq2_title")}</h1>

<div id="columns_container">
    <div class="feedback_block">
        <h3>Feedback 1</h3>
        <div class="yellow_block_square">
            {#if random_layout_state == 0}
                <CartaViewer {carta} value={feedback_AI_body} theme="light" />
            {:else}
                <CartaViewer {carta} value={feedback_human_body} />
            {/if}
        </div>
    </div>
    <div class="feedback_block">
        <h3>Feedback 2</h3>
        <div class="yellow_block_square">
            {#if random_layout_state == 0}
                <CartaViewer {carta} value={feedback_human_body} />
            {:else}
                <CartaViewer {carta} value={feedback_AI_body} />
            {/if}
        </div>
    </div>
</div>

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
    h3 {
        text-align: center;
        font-size: 1.5em;
        font-weight: 600;
        color: rgba(0, 0, 0, 0.6);
    }

    #columns_container {
        display: flex;
        gap: 16px;
        margin-top: 16px;
        margin-bottom: 16px;
        flex-wrap: wrap;
    }
    @media (min-width: 850px) {
        #columns_container {
            flex-wrap: nowrap;
        }
    }

    .feedback_block {
        flex: 100%;
        background-color: #efefef73;
        overflow-y: scroll;
        padding-top: 16px;
        border: solid 1px #e6e6e6;
        border-radius: 8px;
    }

    .yellow_block_square {
        background-color: #ffffdf;
        overflow-y: scroll;
        margin-top: 16px;
        padding: 16px;
        border-top: solid 1px #e4d900;
    }
    @media (min-width: 850px) {
        .yellow_block_square {
            height: 300px;
        }
    }

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
