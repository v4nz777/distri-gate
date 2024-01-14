<template>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 789.32 130.98" ref="mainsvg">
    <g id="Layer_8" data-name="Layer 8">
        <!-- Distri G -->
        <g id="layer-distri">
            <path d="M32.66,101.78C34.07,90.35,36,55.5,36,29.15H74.8c17.86,0,33.33,7.51,33.33,33.76,0,38.87-34.42,38.87-38.34,38.87ZM55.53,86.21H65c14.16,0,20.26-10.56,20.26-23.63,0-13.29-7.41-17.86-16.12-17.86H57.38Z" />
            <path d="M117,101.78c1.42-21.45,3.16-43,3.16-72.63h23.63c-2,24.17-2.83,48.46-2.94,72.63Z" />
            <path d="M205.71,47c-4.91-2-10.46-3.6-15.8-3.6-3.37,0-9.8,1.2-9.8,5.78,0,8.6,25.81,16.66,25.81,32.78,0,7.4-5.22,21.12-28.53,21.12a120.61,120.61,0,0,1-21.67-2.39l-1.63-18c5.66,2.5,12.41,4.79,18.73,4.79,3.59,0,10.23-.65,10.23-5.66,0-8.39-25.81-17.1-25.81-34.09,0-5,2.94-19.93,27.66-19.93a104.41,104.41,0,0,1,19.39,2.07Z" />
            <path d="M280.52,29.15l-.65,16.12c-.87-.11-14.16-.55-22.54-.55C256,62,255,88.17,254.93,101.78H231.52c1.74-17.42,2.94-35.06,3.15-57.06-7.51,0-15,.33-22.65.55l.55-16.12Z" />
            <path d="M308.4,44.39c-1.19,19.06-1.74,38.23-2,57.39H283.9c2.5-22.54,3.38-43.56,3.48-72.63h38.45c5.22,0,26.13.54,26.13,19.27,0,11.44-6.75,17.65-17,21.24,4.25,10.89,9.59,21.34,14.16,32.12H325c-3.93-13.83-9-27.22-14-40.72a30.11,30.11,0,0,0,5.33.54c6.32,0,13.83-2.4,13.83-9.91,0-7.3-7.29-7.3-12.3-7.3Z" />
            <path d="M360.46,101.78c1.42-21.45,3.16-43,3.16-72.63h23.63c-2,24.17-2.83,48.46-2.94,72.63Z" />
    
        </g>
        <g id="layer-g">
            <path d="M487.44,74.56h-9.8l.65-15.25h31.37c-1.09,13.72-1.75,27.34-2.18,41a173.73,173.73,0,0,1-31.8,2.83c-37.57,0-41.49-23.52-41.49-35.17,0-20.37,14.15-40.08,46.06-40.08a132.29,132.29,0,0,1,26.46,2.83l.77,17.1c-7.3-2.29-15-4-22.76-4-15.9,0-27.66,8.28-27.66,25.27,0,12.08,7.4,18.84,19.27,18.84a47.76,47.76,0,0,0,10.46-1.53Z" />
        </g>
        <!-- TE -->
        <g id="layer-te">
            <path d="M694.27,31.52l-.65,16.11c-.87-.11-14.16-.54-22.54-.54-1.31,17.31-2.29,43.45-2.4,57.06H645.27c1.74-17.42,2.94-35.06,3.16-57.06-7.52,0-15,.33-22.66.54l.55-16.11Z" />
            <path d="M760.6,31.52l-.77,16.22c-6.64-.32-13.28-.65-19.82-.65H723.9l-.77,12.74h12.42c6.1,0,12.09-.11,18.19-.33l-1.09,15.9h-30.5l-.76,13.18h7.19c9.8,0,19.6-.33,29.4-.87l-1,16.44H697.65a670.76,670.76,0,0,0,3.7-72.63Z" />
        </g>
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

    const emits = defineEmits(['animationDone'])
    

    onMounted(() => {
        let animationCount = 0

        const animated = document.querySelectorAll(`
        #layer-logo > .logo-triangle,
        #layer-logo > .logo-lines:nth-of-type(1),
        #layer-logo > .logo-lines:nth-of-type(2),
        #layer-logo > .logo-lines:nth-of-type(3),
        #layer-logo,
        #layer-distri,
        #layer-te,
        #layer-g
        `)

        animated.forEach((el)=> {
            
            el.addEventListener('animationend', ()=> {
                animationCount++
                if (animationCount===15)emits('animationDone')
            })
        }) 
    })


</script>

<style scoped>
    
    svg{
         fill: transparent;  /*#841529 */
         animation: logo-fill 1s 4s forwards;
         overflow: visible;
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
        transform: translateX(-130%) scale(2.5);
        animation: logo-fill 700ms 2s, logo-place 700ms 2.8s;
        animation-timing-function: ease-in-out;
        animation-fill-mode: forwards;
    }

    /* TRIANGLE LOGO ENDS */

    /* DISTRI STARTS */

    #layer-distri, #layer-te, #layer-g {
        stroke: black;
        stroke-dashoffset: 410;
        stroke-dasharray: 410;
        animation: form-stroke 3s 2.8s forwards;
        /* display:none; */
    }


    /* DISTRI ENDS */

   
    


    

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

    @keyframes fall {
        to {
            
            transform: translateY(0%);
        }
    }

</style>