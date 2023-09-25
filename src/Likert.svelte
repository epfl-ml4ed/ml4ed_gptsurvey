<script>
    // Likert component in Svelte
    import { _, json } from "svelte-i18n";
    import { RadioButton, RadioButtonGroup } from "carbon-components-svelte";

    export let questions_labels = ["Precise", "Factual", "Fair"];
    export let answers_labels = [
        $_("common_stronglydisagree"),
        $_("common_disagree"),
        $_("common_neutral"),
        $_("common_agree"),
        $_("common_stronglyagree"),
    ];
    export let completed;

    export let answers;
    if (answers === null) {
        answers = new Array(questions_labels.length)
            .fill(null)
            .map(() => Array(answers_labels.length).fill(false));
    }

    function select_answer(i, j) {
        // Ensure only one answer per row
        answers[i] = answers[i].fill(false);
        answers[i][j] = true;
    }

    // Completed if at least one true per row
    $: completed = answers.every((r) => r.some((b) => b));
</script>

<!-- Grid like likert in svelte with ratio buttons -->
<div
    id="grid"
    style={"grid-template-columns:" + "1fr ".repeat(answers_labels.length + 1)}
>
    <div>{" "}</div>
    {#each answers_labels as a_label}
        <div class="table_top_label">{a_label}</div>
    {/each}
    {#each questions_labels as q_label, i}
        <div class="table_side_label">{q_label}</div>
        {#each answers_labels as _, j}
            <div class="table_cell">
                <RadioButton
                    checked={answers[i][j]}
                    on:change={() => select_answer(i, j)}
                />
            </div>
        {/each}
    {/each}
</div>

<style>
    #grid {
        display: grid;
        margin: 8px;
        margin-top: 16px;
    }
    .table_top_label {
        display: flex;
        text-align: center;
        margin-bottom: 16px;
        align-items: center;
        justify-content: center;
        font-weight: 600;
    }
    .table_side_label {
        display: flex;
        text-align: center;
        margin-top: 16px;
        margin-bottom: 16px;
        align-items: center;
        justify-content: center;
        font-weight: 600;
    }
    .table_cell {
        display: flex;
        text-align: center;
        align-items: center;
        justify-content: center;
    }
</style>
