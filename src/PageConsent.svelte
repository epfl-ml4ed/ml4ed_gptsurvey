<script>
    import { _ } from "svelte-i18n";
    import { Checkbox } from "carbon-components-svelte";
    import { NumberInput } from "carbon-components-svelte";

    import { ContentSwitcher, Switch } from "carbon-components-svelte";

    export let bottom_bar_next_enabled;

    let agree = false;
    let over18 = false;
    let sciper = undefined;
    let sciper_range_invalid = true;
    $: sciper_range_invalid = !sciper || sciper < 100000 || sciper > 999999;
    $: bottom_bar_next_enabled = agree && over18 && !sciper_range_invalid;
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
    bind:value={sciper}
    bind:invalid={sciper_range_invalid}
    invalidText={$_("pageconsent_sciper_invalid")}
/>
<br />
<br />
<ContentSwitcher style="height:60px" selectedIndex={2}>
    <Switch style="white-space: normal" text={$_("common_stronglydisagree")} />
    <Switch style="white-space: normal" text={$_("common_disagree")} />
    <Switch style="white-space: normal" text={$_("common_neutral")} />
    <Switch style="white-space: normal" text={$_("common_agree")} />
    <Switch style="white-space: normal" text={$_("common_stronglyagree")} />
</ContentSwitcher>

<style>
    #title {
        margin-top: 8px;
        margin-bottom: 8px;
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
