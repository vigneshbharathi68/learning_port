<template>
<nav class="flex flex-col border-0 bg-gradient-to-b from-teal-600 via-purple-600 to-indigo-900 max-w-56 h-screen px-2 overflow-y-scroll scrollbar-thin scrollbar-track-teal-200 scrollbar-thumb-teal-400">
    
    <div class="flex flex-col w-52 mt-2 p-2 justify-start rounded rounded-lg bg-gray-900 bg-opacity-25">
        <div class="">
            <!-- <img :src="$static.path(require('@/assets/profile-pic.png'))" class="w-14 h-14 rounded-full" /> -->
        </div>
        <div @click="toggleMenu = !toggleMenu" class="pt-3">
            <div class="font-semibold text-white truncate">{{ Username }}</div>
            <p class="text-teal-300 text-sm xl:text-xs hover:text-green-400">Researcher</p>
        </div>

         <div v-if=" toggleMenu " class="flex flex-col absolute w-52 rounded rounded-md overflow-x-hidden select-none z-50">
            <li v-on:click="toggleLogOutModal()" class="px-4 py-3 text-gray-100 flex flex-row border-gray-300 hover:text-gray-700 hover:bg-gray-100 hover:font-bold rounded rounded-md cursor-pointer">
                <span>
                    <i class="fas fa-sign-out-alt"></i>
                </span>
                <a>
                    <span class="ml-2">Logout</span>
                </a>
            </li>
        </div>
    </div>


    <div class="realtive mt-4 p-1 rounded rounded-lg bg-gray-900 bg-opacity-25">
        <ul class="text-sm">
            
            <!-- Dashboard -->
            
                <li :class=' { "active": selected == "0" } ' 
                class="mb-1 px-4 py-3 text-gray-100 flex flex-row border-gray-300 hover:text-black hover:bg-gray-100 hover:font-semibold rounded hover:rounded-md border-b border-gray-200 border-opacity-25">
                    <span>
                        <svg class="fill-current h-5 w-5" viewBox="0 0 24 24">
                            <path d="M16 20h4v-4h-4m0-2h4v-4h-4m-6-2h4V4h-4m6
                            4h4V4h-4m-6 10h4v-4h-4m-6 4h4v-4H4m0 10h4v-4H4m6
                            4h4v-4h-4M4 8h4V4H4v4z" />
                        </svg>
                    </span>
                        <span class="ml-2 outline-none">Dashboard</span>
                </li>
            
            
            <!-- Bot click -->
            <li @click="isBot = !isBot; isCollection = false" :class=' { "active": selected == "1" } ' 
            class="mb-1 px-4 py-3 text-gray-100 flex flex-row border-gray-300 select-none hover:text-black hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25 cursor-pointer">
                <span>
                    <i class="fas fa-project-diagram"></i>
                </span>
                <span class="ml-2">Bot</span>
            </li>

            <div v-if=" isBot " class="flex flex-col absolute w-52 rounded rounded-sm overflow-x-hidden select-none z-50">
                <span v-for="bot_name in bot_list" :key="bot_name" @click.prevent="botArticleClick(bot_name)" 
                :class=" {'dropdown_active': bot_id == bot_name.bot.id} " class="flex bg-gray-200 border-solid border-b-2 border-gray-50 px-3 py-3 text-gray-900 items-center hover:text-indigo-700 hover:bg-gray-300 hover:font-bold cursor-pointer">
                    <span class="mr-2 text-indigo-700">
                        <i class="fas fa-project-diagram"></i>
                    </span>
                    <div class="truncate">{{bot_name.bot.bot_name}}</div>
                </span>
                <span @click.prevent="$browser.openBrowser('https://www.zealbots.com/zbot/new_bot/')" class="border-solid bg-gray-400 flex text-black items-center p-3 hover:text-white hover:bg-gray-500 hover:font-bold cursor-pointer">
                    <span class="mr-2">
                        <i class="fas fa-project-diagram"></i>
                    </span>
                    <span class="truncate">New Bot</span>
                </span>
            </div>

            <!-- Collection -->
            <li @click="isCollection = !isCollection; isBot = false" :class=' { "active": selected == "2" } ' 
            class="mb-1 px-4 py-3 text-gray-100 flex flex-row border-gray-300 select-none hover:text-black hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25 cursor-pointer">
                <span>
                    <i class="fas fa-paste"></i>
                </span>
                <span class="ml-2">Collection</span>
            </li>

            <div v-if="isCollection " class="absolute w-52 bg-gray-400 rounded rounded-sm overflow-hidden select-none z-50">
                <span v-for="collection_name in collection_list" :key="collection_name" @click.prevent="collectionArticleClick(collection_name)" 
                :class="{ 'dropdown_active': collection_id == collection_name.id }" class="flex bg-gray-200 border-solid border-b-2 border-gray-50 px-4 py-3 text-gray-800 items-center hover:text-indigo-800 hover:bg-gray-300 hover:font-bold cursor-pointer">
                    <span class="mr-2 text-indigo-800">
                        <i class="fas fa-paste"></i>
                    </span>
                    <span class="truncate" v-text="collectionNameSplit(collection_name.name)"></span>
                </span>
            </div>
            
            
            <!-- Citeman -->
            <li @click="isCiteman = !isCiteman"  :class=' { "active": selected == "3" } ' 
            class="mb-1 px-4 py-3 text-gray-100 flex flex-row border-gray-300 hover:text-black hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25 cursor-pointer">
                <span>
                    <i class="fas fa-quote-right"></i>
                </span>
                <span class="ml-2">Citeman</span>
            </li>            
            <div v-if="isCiteman" class="absolute w-52 z-50 bg-gray-200 rounded rounded-sm overflow-hidden select-none">
                <span v-for="Citeman_name in Citeman_list" :key="Citeman_name" @click.prevent="citemanArticleClick(Citeman_name)" class="p-3 bg-gray-200 border-solid border-b-2 border-gray-50 flex text-gray-900 items-center hover:text-black hover:bg-gray-300 hover:font-bold cursor-pointer">
                    <span class="mr-2 text-indigo-800"> <i class="fas fa-quote-right"></i> </span>
                    <span class="truncate" v-text="collectionNameSplit(Citeman_name.name)"></span>
                </span>
            </div>
            
            <!-- Todo Tasks -->
            
                <li :class=' { "active": selected == "10" } ' 
                class=" flex flex-row mb-1 px-4 py-3 text-gray-100 border-gray-300 hover:text-gray-800 hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25">
                    <span> <i class="fas fa-list"></i> </span>
                    <span class="ml-2">Tasks</span>
                </li>
            



            <!-- Zkloud -->
            
                <li :class=' { "active": selected == "5" } ' 
                class="flex flex-row mb-1 px-4 py-3 text-gray-100 border-gray-300 hover:text-gray-700 hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25">
                    <span>
                        <i class="fas fa-cloud"></i>
                    </span>
                    <span class="ml-2">Zkloud</span>
                </li>
            


            <!-- Plugin -->
            
            <li :class=' { "active" : selected == "7" } ' 
            class="mb-1 px-4 py-3 text-gray-100 flex flex-row border-gray-300 hover:text-black hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25">
                <span>
                    <i class="fas fa-swatchbook"></i>
                </span>
                <span class="ml-2">Plugins</span>
            </li>
            

            <!-- Settings  -->
            
            <li :class=' { "active" : selected == "6" } ' 
            class="mb-1 px-4 py-3 text-gray-100 flex flex-row border-gray-300 hover:text-black hover:bg-gray-100 hover:font-bold rounded hover:rounded-md border-b border-gray-200 border-opacity-25">
                <span>
                    <i class="fas fa-users-cog"></i>
                </span>
                <span class="ml-2">Settings</span>
            </li>
            


            <!-- Log out -->
            <li v-on:click="toggleLogOutModal()" class="px-4 py-3 text-gray-100 flex flex-row border-gray-300 hover:text-gray-700 hover:bg-gray-100 hover:font-bold rounded rounded-md cursor-pointer">
                <span>
                    <i class="fas fa-sign-out-alt"></i>
                </span>
                <a>
                    <span class="ml-2">Logout</span>
                </a>
            </li>
        </ul>
    </div>

    <!-- Logout pop-up -->
    <div v-if="showLogOutModal" class="overflow-x-hidden overflow-y-auto bg-black bg-opacity-60 fixed inset-0 z-50 outline-none focus:outline-none justify-center lg:justify-end items-center flex">
        <div class="relative w-auto my-6 mx-auto max-w-sm">
            <!--content-->
            <div class="rounded-md shadow-2xl relative flex flex-col overflow-hidden w-full bg-white outline-none focus:outline-none">
                <!--header-->
                <div class="flex bg-gradient-to-r from-green-600 via-purple-700 to-blue-800 text-white items-start justify-center p-4 border-b border-solid border-gray-300">
                    <h3 class="text-xl font-semibold">Please confirm</h3>
                </div>
                <!--body-->
                <div class="relative pl-8 pr-8 pt-4 pb-4 flex-auto">
                    <p class="my-4 text-gray-700 text-md leading-relaxed">
                        Are you sure want to log out?
                    </p>
                </div>
                <!--footer-->
                <div class="flex gap-8 items-center justify-center pb-6">
                    <button class="max-w-24 w-24 text-teal-500 bg-transparent border border-solid border-teal-500 hover:bg-teal-500 hover:text-white active:bg-red-600 font-bold uppercase text-sm px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1" type="button" style="transition: all .15s ease" v-on:click="toggleLogOutModal()">Cancel</button>
                    <button class="max-w-24 w-24 text-red-500 bg-transparent border border-solid border-red-500 hover:bg-red-500 hover:text-white active:bg-red-600 font-bold uppercase text-sm px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1" type="button" style="transition: all .15s ease" v-on:click="submit">Exit</button>
                </div>
            </div>
        </div>
    </div>

    <div class="grid grid-cols-1 place-content-end h-full mb-1">
        <div class="flex flex-col place-content-end w-52 mt-2 p-1 justify-start rounded rounded-lg bg-gray-800 bg-opacity-30">
            <div class="">
                <!-- <img :src="$static.path(require('@/assets/faq.svg'))" class="bg-white w-52 rounded-md" /> -->
            </div>
            <div class="flex flex-col p-3 justify-center conter-center">
                <div class="font-semibold text-white truncate">Need help?</div>
                <p class="text-teal-300 text-sm xl:text-xs hover:text-green-400">Read Documentation</p>
            </div>
        </div>
    </div>
    <div class="mb-4">
        <div class="flex flex-col w-52 rounded rounded-lg bg-gray-800 bg-opacity-50">
            <div class="flex flex-col p-3 justify-center content-center">
                <p class="tracking-wider text-gray-50 text-xs lg:text-md xl:text-xs hover:text-green-400">www.zealbots.com</p>
            </div>
        </div>
    </div>
</nav>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      bot_list: [],
      collection_list: [],
      showLogOutModal: false,
      isBot: false,
      isCollection: false,
      isCiteman: false,
      Citeman_list:[],
      toggleMenu: false,
      Username: "Vignesh Bharathi"
    }
  },
  props:{
    selected: String,
    bot_id: String,
    collection_id: String,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
