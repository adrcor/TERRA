<template>
    <footer class="flex flex-row text-on-background gap-6 py-3 text-sm">
        <a href="mailto:trivia.terra@gmail.com" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/envelope.svg" class="w-4 h-4"/>
            <p>Contact</p>
        </a>
        <a href="https://github.com" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/github.svg" class="w-4 h-4"/>
            <p>Github</p>
        </a>
        <router-link to="privacy-policy" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/lock.svg" class="w-4 h-4"/>
            <p>Privacy Policy</p>
        </router-link>
        <router-link to="terms-and-conditions" class="flex flex-row items-center gap-1 opacity-30 hover:opacity-60 active:opacity-30">
            <img src="@/assets/icons/solid/doc.svg" class="w-4 h-4"/>
            <p>Terms and Condition</p>
        </router-link>
    </footer>
</template>