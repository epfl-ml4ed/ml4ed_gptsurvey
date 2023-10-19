<script>
    import { _ } from "svelte-i18n";
    import { Carta, CartaViewer } from "carta-md";
    import { math } from "@cartamd/plugin-math";
    import Likert from "./Likert.svelte";

    const carta = new Carta({
        extensions: [math()],
    });

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let feedback_AI_body;
    export let feedback_human_body;

    export let likert_AI;
    export let likert_human;
    export let extra_likert_AI;
    export let extra_likert_human;

    // Pseudo random : if sciperID is even then random_layout_state is 0 else 1
    let random_layout_state = sciperID % 2;
    // Likert completed
    let likert_AI_completed;
    let likert_human_completed;
    let extra_likert_AI_completed;
    let extra_likert_human_completed;

    let extra_questions_labels = ["Trustworthy", "Reliable", "Ethical"];

    $: bottom_bar_next_enabled =
        likert_AI_completed &&
        likert_human_completed &&
        extra_likert_AI_completed &&
        extra_likert_human_completed;

    let feeback1_real_name =
        random_layout_state == 0
            ? $_("pageq3_AI") + " 🤖"
            : $_("pageq3_human") + " 🤓";
    let feeback2_real_name =
        random_layout_state == 0
            ? $_("pageq3_human") + " 🤓"
            : $_("pageq3_AI") + " 🤖";
</script>

<h1 id="title">{$_("pageq3_title")}</h1>
<div id="block">
    <p>{$_("pageq3_source")}</p>
    <br />
    <p>{$_("pageq3_txt1") + " "}<b>{feeback1_real_name}</b></p>
    <br />
    <p>{$_("pageq3_txt2") + " "}<b>{feeback2_real_name}</b></p>
</div>

<p>{$_("pageq3_txt3") + " :"}</p>
<div id="columns_container">
    <div class="feedback_block">
        <h3>Feedback 1</h3>
        <h4 style="text-align:center">{feeback1_real_name}</h4>
        <div class="yellow_block_square">
            {#if random_layout_state == 0}
                <CartaViewer {carta} value={feedback_AI_body} />
            {:else}
                <CartaViewer {carta} value={feedback_human_body} />
            {/if}
        </div>
        <div
            style="background-color:white;margin:8px;border-radius:8px;padding:8px;border:solid 1px #e6e6e6"
        >
            <p style="margin-left:16px;margin-right:16px;font-weight:800">
                {$_("pageq3_fb")
                    .replace("[SOURCE]", feeback1_real_name)
                    .replace("[FEEDBACK_IDX]", "1")}
            </p>
        </div>
        {#if random_layout_state == 0}
            <Likert
                bind:answers={likert_AI}
                bind:completed={likert_AI_completed}
            />
        {:else}
            <Likert
                bind:answers={likert_human}
                bind:completed={likert_human_completed}
            />
        {/if}
        <br />
        <div style="border-top: solid 1px #dbdbdb" />
        <br />
        <div
            style="background-color:white;margin:8px;border-radius:8px;padding:8px;border:solid 1px #e6e6e6"
        >
            {#if random_layout_state == 0}
                <p style="margin-left:16px;margin-right:16px;font-weight:800">
                    {$_("pageq3_AI_q")}
                </p>
            {:else}
                <p style="margin-left:16px;margin-right:16px;font-weight:800">
                    {$_("pageq3_human_q")}
                </p>
            {/if}
        </div>
        {#if random_layout_state == 0}
            <Likert
                questions_labels={extra_questions_labels}
                bind:answers={extra_likert_AI}
                bind:completed={extra_likert_AI_completed}
            />
        {:else}
            <Likert
                questions_labels={extra_questions_labels}
                bind:answers={extra_likert_human}
                bind:completed={extra_likert_human_completed}
            />
        {/if}
    </div>
    <div class="feedback_block">
        <h3>Feedback 2</h3>
        <h4 style="text-align:center">{feeback2_real_name}</h4>
        <div class="yellow_block_square">
            {#if random_layout_state == 0}
                <CartaViewer {carta} value={feedback_human_body} />
            {:else}
                <CartaViewer {carta} value={feedback_AI_body} />
            {/if}
        </div>
        <div
            style="background-color:white;margin:8px;border-radius:8px;padding:8px;border:solid 1px #e6e6e6"
        >
            <p style="margin-left:16px;margin-right:16px;font-weight:800">
                {$_("pageq3_fb")
                    .replace("[SOURCE]", feeback2_real_name)
                    .replace("[FEEDBACK_IDX]", "2")}
            </p>
        </div>
        {#if random_layout_state == 0}
            <Likert
                bind:answers={likert_human}
                bind:completed={likert_human_completed}
            />
        {:else}
            <Likert
                bind:answers={likert_AI}
                bind:completed={likert_AI_completed}
            />
        {/if}
        <br />
        <div style="border-top: solid 1px #dbdbdb" />
        <br />
        <div
            style="background-color:white;margin:8px;border-radius:8px;padding:8px;border:solid 1px #e6e6e6"
        >
            {#if random_layout_state == 0}
                <p style="margin-left:16px;margin-right:16px;font-weight:800">
                    {$_("pageq3_human_q")}
                </p>
            {:else}
                <p style="margin-left:16px;margin-right:16px;font-weight:800">
                    {$_("pageq3_AI_q")}
                </p>
            {/if}
        </div>
        {#if random_layout_state == 0}
            <Likert
                questions_labels={extra_questions_labels}
                bind:answers={extra_likert_human}
                bind:completed={extra_likert_human_completed}
            />
        {:else}
            <Likert
                questions_labels={extra_questions_labels}
                bind:answers={extra_likert_AI}
                bind:completed={extra_likert_AI_completed}
            />
        {/if}
    </div>
</div>

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

    b {
        font-style: italic;
        font-weight: 600;
    }

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
        padding-bottom: 16px;
        border: solid 1px #e6e6e6;
        border-radius: 8px;
    }

    .yellow_block_square {
        background-color: #ffffdf;
        overflow-y: scroll;
        margin-top: 16px;
        margin-bottom: 16px;
        padding: 16px;
        border-top: solid 1px #e4d900;
        border-bottom: solid 1px #e4d900;
    }
    @media (min-width: 850px) {
        .yellow_block_square {
            height: 300px;
        }
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

    :global(.markdown-body) {
        background-color: transparent;
    }

    :global(.markdown-body pre) {
        background-color: #ff780017;
        font-weight: bold;
    }

    :global(.markdown-body *) {
        list-style: revert;
    }
</style>
