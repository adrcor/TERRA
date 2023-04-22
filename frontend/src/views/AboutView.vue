<template>
    <body class="flex flex-col gap-16 w-2/3 text-on-background text-opacity-60 py-8">
        
        <div class="flex flex-col gap-12">
            <div class="flex flex-row gap-2 self-center items-center">
                <img src="@/assets/icons/color/terra.svg" class="w-12 h-12"/>
                <h1 class="text-primary text-4xl">TerraTrivia</h1>
            </div>
            
            <p>Welcome to TerraTrivia! This website is designed to help you learn and master the capitals of every country in the world through two different modes.</p>
        </div>

        <div class="flex flex-col gap-2">
            <h2 class="text-primary text-2xl">Practice</h2>
        
            <p>Whether you're just starting to learn world capitals or you're already an expert, the practice mode will help you to improve your knowledge by focusing on your weaknesses.</p>

            <p>At first, you'll be presented with a set of five countries, one after the other, and you'll need to type their corresponding capitals as quickly as possible. The algorithm will prioritize the countries that you have the most difficulty with, so you can improve your knowledge faster. As you become more comfortable with the current selection of countries, we'll gradually add new ones to the pool, so you can continue to challenge yourself.</p>
        </div>
        <div class="flex flex-col gap-2">
            <h2 class="text-primary text-2xl">Practice stats</h2>
            
            <p>Throughout the practice mode, you'll be able to track your progress and familiarity with each country through three stats:</p>
            
            <ul class="px-4">
                <li>- Reaction: This measures the time it takes you, in milliseconds, to type the first correct characters of the expected capital.</li>
                <li>- Typing: This measures the speed you need, in words per minute (wpm), to type out the country's capital. It's calculated by dividing the number of words (one word is considered to be 5 characters, including spaces) by the time it takes between the first correct characters being typed and the full capital being typed.</li>
                <li>- Score: Each country is assigned a score based on your mean reaction time and mean typing speed. A score of 50% can be attained with a reaction time of 2 seconds and a typing speed of 30wpm, which will count the country as validated. Once all available countries are validated, new ones will be added to the pool. To reach 100%, you'll need a reaction time of 700 milliseconds and a typing speed of 100wpm.</li>
            </ul>
        </div>

        <div class="flex flex-col gap-2">
            <h2 class="text-primary text-2xl">Test</h2>
    
            <p>The test mode allows you to put your knowledge to the test with timed challenges. You will be presented with a selected number of countries, one after the other, and your goal is to type their corresponding capitals as quickly and accurately as possible.</p>

            <p>Your final score will be calculated based on the number of correct answers per minute. All of your test results will be saved, allowing you to visualize your progress over time and compare your performance across the different regions in the account section.</p>
        </div>
    </body>
</template>