<script>
    import { _ } from "svelte-i18n";
    import { Carta, CartaViewer } from "carta-md";
    import { math } from "@cartamd/plugin-math";
    import "github-markdown-css/github-markdown-light.css";
    import "katex/dist/katex.css";
    import Likert from "./Likert.svelte";

    const carta = new Carta({
        extensions: [math()],
    });

    export let bottom_bar_next_enabled;
    export let sciperID;
    export let course_name;
    export let task_name;
    export let task_body;
    export let answer_body;
    export let feedback_AI_body;
    export let feedback_human_body;

    export let likert_AI;
    export let likert_human;

    // Pseudo random : if sciperID is even then random_layout_state is 0 else 1
    let random_layout_state = sciperID % 2;
    // Likert completed
    let likert_AI_completed;
    let likert_human_completed;

    $: bottom_bar_next_enabled = likert_AI_completed && likert_human_completed;
</script>

<h1 id="title">{$_("pageq1_title")}</h1>
<p>
    {$_("pageq1_txt1_fragment1") + " "}<i>{task_name}</i>{" " +
        $_("pageq1_txt1_fragment2") +
        " "}<i>{course_name}</i>{" :"}
</p>
<div class="yellow_block">
    <CartaViewer {carta} value={task_body} />
</div>
<p>{$_("pageq1_txt2") + " :"}</p>
<div class="yellow_block">
    <CartaViewer {carta} value={answer_body} />
</div>
<p>{$_("pageq1_txt3") + " :"}</p>
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
        <div
            style="background-color:white;margin:8px;border-radius:8px;padding:8px;border:solid 1px #e6e6e6"
        >
            <p style="margin-left:16px;margin-right:16px;font-weight:800">
                {$_("pageq1_fb_1")}
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
        <div
            style="background-color:white;margin:8px;border-radius:8px;padding:8px;border:solid 1px #e6e6e6"
        >
            <p style="margin-left:16px;margin-right:16px;font-weight:800">
                {$_("pageq1_fb_2")}
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

    i {
        font-style: italic;
    }

    h3 {
        text-align: center;
        font-size: 1.5em;
        font-weight: 600;
        color: rgba(0, 0, 0, 0.6);
    }

    .yellow_block {
        background-color: #ffffdf;
        overflow-y: scroll;
        margin-top: 16px;
        margin-bottom: 16px;
        padding: 16px;
        border: solid 1px #e4d900;
        border-radius: 8px;
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
