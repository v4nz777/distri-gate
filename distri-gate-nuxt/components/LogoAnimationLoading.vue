<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 789.32 130.98">
    <g id="Layer_8" data-name="Layer 8">
    
        <g id="layer-logo">
            <path class="logo-triangle" d="M586.91,51.61l-3.16-4.34-13-17.85L557.87,47.27l-3.15,4.34L549,59.54l-3.11,4.29L541,70.59,537.78,75,518.7,101.36l104.18-.2ZM543.24,75l3.2-4.42,4.89-6.76,3.11-4.29,5.74-7.93,3.14-4.34,7.47-10.33,7.5,10.33,3.16,4.34,5.75,7.93,3.12,4.29,23.9,32.93-86.85.17Z" />
            <path class="logo-triangle" d="M548.2,88.31,570.89,57l22.69,31.25ZM570.89,64,556.33,84.14l29.12,0Z" />
            <rect class="logo-lines" x="518.62" y="47.27" width="104.46" height="4.35" />
            <rect class="logo-lines" x="518.62" y="59.54" width="71.91" height="4.29" />
            <rect class="logo-lines" x="518.62" y="70.59" width="44.43" height="4.42" />
        </g>
    </g>
    </svg>
</template>

<script setup lang="ts">

</script>

<style scoped>
    
    svg{
         fill: transparent;  /*#841529 */
         animation: logo-fill 1s 4s forwards;
    }

    /* TRIANGLE LOGO STARTS */

    #layer-logo > .logo-triangle {
        stroke-dashoffset: 310;
        stroke-dasharray: 310;
        animation: form-stroke 2s forwards
    }

    #layer-logo > .logo-lines:nth-of-type(1) {
        transform: translateX(-225%);
        animation: appear-logo-lines 500ms;
        animation-delay: 1s;
        animation-fill-mode: forwards;
    }

    #layer-logo > .logo-lines:nth-of-type(2) {
        transform: translateX(-225%);
        animation: appear-logo-lines 500ms;
        animation-delay: 1300ms;
        animation-fill-mode: forwards;
    }
    #layer-logo > .logo-lines:nth-of-type(3) {
        transform: translateX(-225%);
        animation: appear-logo-lines 500ms;
        animation-delay: 1600ms;
        animation-fill-mode: forwards;
    }

    #layer-logo {
        stroke:black;
        transform: translateX(-25%);
        animation: logo-fill 700ms 2s forwards, logo-fill 1000ms 2.5s infinite;
        animation-timing-function: ease-in-out;
    }


    


    

    @keyframes form-stroke {
        to {
            stroke-dashoffset: 0;
            /* stroke-dasharray: 0; */
        }
    }

    @keyframes appear-logo-lines{
        to {
            transform: translateX(0%);
        }
    }

    @keyframes logo-fill {
        50% {
            fill: #d46238;
        }

        100% {
            fill: #841529;
            stroke-width: 0;
        }
    }

    @keyframes logo-place {
        50% {
            transform: translateY(-20%)
        }
        100% {
            
            transform: translateX(0%);
        }
    }



</style>