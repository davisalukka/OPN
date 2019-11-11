<template>
    <div> 
     <div class="wrapper_for_sign_in">
        <div class="opn-logo">
           <a href="#"><img src="images/opn.png" alt="OPN" /></a>
        </div>
    <!-- Form -->
    <form class="login" @submit.prevent="login">
        <h1>Sign in</h1> 
        <!-- <label>Username</label> -->
        <input required v-model="username" type="username" name="textfield username" class="textfield" placeholder="Name"/>
        <!-- <label>Password</label> -->
        <input required v-model="password" type="password" name="textfield password" class="textfield" placeholder="Password"/>
            <!-- <hr/> -->
    <button type="submit" class="register-btn" >Login</button> 

    <ul v-if="errors && errors.length" class="error_message">
        <li 
            <p>Error. Invalid login credentials</p>
        </li>
    </ul>
        <div class="box">
            Not registered? <a class="not-register" name="not-register" href="#"><router-link to="register">Create an account</router-link></a>
        </div>
    </form>
     </div>
 </div>
</template>

<style>
 body {
     font-family: 'Poppins', sans-serif;
 }

 .wrapper_for_sign_in {
     width: 600px;
     margin: 10px auto 0;
 }

 .opn-logo {
     text-align: center;
 }
 .error_message {
     text-align: center;
     color: red;
     list-style-type: none;
     padding: 0;
     margin: 0;
 }
 h1 {
     color: #000102;
     font-size: 32px;
     font-weight: 300;
     line-height: 56px;
     text-align: center;
     text-transform: uppercase;
 }
 .textfield {
     width: 60%;
     font-size: 14px;
     height: 40px;
     border: 1px solid #eaeaea;
     padding: 0 5px 0 10px;
     margin: 0 auto 20px;
     display: block;
 }
 .box {
     width: 100%;
     text-align: center;
     margin: 15px 0;
 }
 .not-register {
     font-size: 14px;
     line-height: 30px;
     color: #25aae1;
     padding: 10px;
     text-decoration: underline;
 }
 .not-register:hover {
     color: #25aae1;
 }
 .register-btn {
     font-size: 18px;
     background: #f59331;
     color: #fff;
     padding: 10px 0;
     border: none;
     width: 63%;
     margin: 0 auto;
     display: block;
 }
 /* ==== MEDIA QUERIES ==== */
 @media screen and (max-width: 768px) {
     .wrapper_for_sign_in {
         width: 90%;
         padding: 0 5%;
     }
     .textfield {
         width: 80%;
     }
     .register-btn {
         width: 84%;
     }
 }

</style>

<script>
    export default {
        data() {
            return {
                "username": "",
                "email": "", 
                "password": "",
                errors: []

            }
        },
        methods: {
            login: function() {
                let username = this.username
                let password = this.password
                this.$store.dispatch('login', {username, password })
                .then(() => this.$router.push('/dashboard'))
                .catch(err => {
                this.errors.push(err)})//console.log(err))
            }
        }
    }
</script>
