<script>
    import { _ } from "svelte-i18n";
    import { Checkbox } from "carbon-components-svelte";
    import { NumberInput } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;
    export let sciperID;

    let agree = false;
    let over18 = false;
    let sciperID_range_invalid = true;
    $: sciperID_range_invalid =
        !sciperID || sciperID < 100000 || sciperID > 999999;
    $: bottom_bar_next_enabled = agree && over18 && !sciperID_range_invalid;
</script>

<h1 id="title">{$_("pageconsent_title")}</h1>
<p style="margin-bottom">{$_("pageconsent_text")}</p>
<br />
<br />
<Checkbox
    bind:checked={agree}
    id="agree"
    labelText={$_("pageconsent_checkbox_agree")}
/>
<br />
<br />
<Checkbox
    bind:checked={over18}
    id="over18"
    labelText={$_("pageconsent_checkbox_over18")}
/>
<br />
<br />
<p>{$_("pageconsent_sciper")}</p>
<br />
<br />
<NumberInput
    hideSteppers
    label="SCIPER"
    bind:value={sciperID}
    bind:invalid={sciperID_range_invalid}
    invalidText={$_("pageconsent_sciper_invalid")}
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
</style>
