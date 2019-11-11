<template>
  <footer class="footer">
    <div class="container">
      <nav>
        <ul>
          <li>
            <a href="https://opn.ninja">Open People Network</a>
          </li>
          <li>
            <a href="https://opn.ninja/meet-the-team/">
                              About Us
            </a>
          </li>
          <li>
            <a href="https://opn.ninja/news/">
              News
            </a>
          </li>
          <li>
            <a href="https://opn.ninja/sponsors-and-partners/">
              Links
            </a>
          </li>
        </ul>
      </nav>
      <!-- 
      -->
    </div>
  </footer>
</template>
<script>
export default {
    computed: {
        isLoggedIn: function(){ return this.$store.getters.isLoggedIn}
    },
    methods: {
        logout: function() {
            this.$store.dispatch('logout')
            .then(() => {
                this.$router.push('/login')
            })
        }
    },
};
</script>
<style>
</style>
