<script>
    import { _, locale } from "svelte-i18n";
    import { Button } from "carbon-components-svelte";

    let lang = "en";
    $: btn_1_kind = lang == "en" ? "primary" : "tertiary";
    $: btn_2_kind = lang == "en" ? "tertiary" : "primary";
    $: if (lang == "en") {
        locale.set("en-US");
    }
    $: if (lang == "fr") {
        locale.set("fr");
    }
</script>

<h1 id="title">{$_("pagewelcome_title")}</h1>
<div id="lang_selector" style="display:none;">
    <p style="text-align: center;margin-bottom: 8px">
        {$_("pagewelcome_lang")}
    </p>
    <Button size="small" kind={btn_1_kind} on:click={() => (lang = "en")}
        >English</Button
    >
    <Button size="small" kind={btn_2_kind} on:click={() => (lang = "fr")}
        >Français</Button
    >
</div>
<p style="margin-top:32px">
    {$_("pagewelcome_intro1")}
    <a
        href="https://drive.google.com/file/d/1x2Z1pPcXhxwjZMmTaeIPI3DNQU-93cwK/view?usp=sharing"
        >{$_("pagewelcome_intro2")}</a
    >
    {$_("pagewelcome_intro3")}
</p>

<style>
    #title {
        margin-top: 0px;
        margin-bottom: 8px;
        text-align: center;
    }

    p {
        white-space: pre-line;
        text-align: justify;
    }

    #lang_selector {
        width: 300px;
        margin: auto;
        text-align: center;
        margin-bottom: 16px;
    }
</style>
