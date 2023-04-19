<template>
    <footer class="flex flex-row text-on-background gap-8 py-3 text-sm select-none">
        <a href="mailto:trivia.terra@gmail.com" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/envelope.svg" class="w-4 h-4"/>
            <p class="hidden sm:block">Contact</p>
        </a>
        <a href="https://github.com/adrcor/terra" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/github.svg" class="w-4 h-4"/>
            <p class="hidden sm:block">Github</p>
        </a>
        <router-link to="privacy-policy" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/lock.svg" class="w-4 h-4"/>
            <p class="hidden sm:block">Privacy Policy</p>
        </router-link>
        <router-link to="terms-and-conditions" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/doc.svg" class="w-4 h-4"/>
            <p class="hidden sm:block">Terms and Condition</p>
        </router-link>
    </footer>
</template>