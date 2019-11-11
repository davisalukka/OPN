<template>
    <div class="wrapper_register_page">
        <!-- <h4>Register</h4> -->
        <div class="opn-logo">
            <a href="#"><img src="images/opn.png" alt="OPN" /></a>
        </div>
        <h1>Sign up</h1>
        <!-- Form -->
        <form @submit.prevent="register">
            <!-- <label for="name">Username</label> -->
            <div>
                <input id="name" type="text" v-model="name" class="textfield" placeholder="Username" required autofocus>
            </div>
            <!-- <label for="email" >E-Mail Address</label> -->
            <div>
                <input id="email" type="email"
                v-model="email" class="textfield" placeholder="Email" required>
            </div>
            <!-- <label for="password">Password</label> -->
            <div>
                <input
                id="password"
                type="password"
                v-model="password"
                class="textfield"
                placeholder="Password"
                required>
            </div>
            <!-- <label for="password-confirm">Confirm Password</label>-->
            <div>
                <input
                id="password-confirm"
                type="password"
                v-model="password_confirmation"
                class="textfield"
                placeholder="Confirm Password"
                required>
            </div>
            <div>
                <button
                    type="submit" class="register-btn">Register</button>
                <ul v-if="errors && errors.length" class="error_message">
                    <li 
                        <p>Error. Invalid data entered</p>
                    </li>
                </ul>
            </div>
            <div class="box">
                Have already an account? <a class="not-register" name="not-register" href="#"><router-link
                                                                                     to="login">Login Here</router-link></a>
            </div>
        </form>
    </div>
</template>
<style>
 body {
     font-family: 'Poppins', sans-serif;
 }
 .wrapper_register_page {
     width: 600px;
     margin: 10px auto 0;
 }
 .opn-logo {
     text-align: center;
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
 }

</style>

<script>
    export default {
        data() {
            return {
                name : "",
                email : "", 
                password : "", 
                password_confirmation : "",
                errors: []
                //is_admin : null
            }
        },
        methods: {
            register: function() {
                let data = {
                    username: this.name,
                    email: this.email, 
                    password1: this.password, 
                    password2: this.password_confirmation
                    //is_admin: this.is_admin
                }
                this.$store.dispatch('register', data)
                .then(() => this.$router.push('/'))
                .catch(err => {
                this.errors.push(err)})//console.log(err))
            }
        }
    }
</script>

