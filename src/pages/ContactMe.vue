<template>
  <div>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">

      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail equalize bg-img"
           style="background-image: url(/static/img/bg-img/contact.jpg);"></div>

      <!-- Hero Content -->
      <div class="hero-content equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-8">
              <div class="line"></div>
              <h2>Contact me</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vel tortor
                facilisis, volutpat nulla placerat, tincidunt mi. Nullam vel orci dui.</p>
              <a href="#" v-scroll-to="'#contact-me'" class="btn sonar-btn white-btn">contact
                me</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Hero Area End ***** -->

    <section class="sonar-contact-area section-padding-100" id="contact-me">
      <!-- back end content -->
      <div class="backEnd-content">
        <img class="dots" src="/static/img/core-img/dots.png" alt="">
      </div>

      <div class="container">
        <div class="row">
          <!-- Contact Form Area -->
          <div class="col-12">
            <div class="contact-form text-center">

              <h2>I am an experienced photographer</h2>
              <h4>Let’s talk</h4>

              <form action="#"
                    method="post"
                    @keydown="errors.clear($event.target.name)">
                <div class="row">
                  <div class="col-12 col-md-4">
                    <div class="form-group">
                      <input type="text" class="form-control"
                             name="name"
                             :class="{'is-invalid': errors.has('name')}"
                             v-model="message.name"
                             placeholder="Your Name">
                      <small class="text-danger" v-if="errors.has('name')">
                        {{ errors.get('name') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12 col-md-4">
                    <div class="form-group">
                      <input type="tel" class="form-control"
                             name="phone"
                             :class="{'is-invalid': errors.has('phone')}"
                             v-model="message.phone"
                             placeholder="Your Phone"
                              v-mask="'+38(###) ###-##-##'">
                      <small class="text-danger" v-if="errors.has('phone')">
                        {{ errors.get('phone') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12 col-md-4">
                    <div class="form-group">
                      <input type="email" class="form-control"
                             name="email"
                             :class="{'is-invalid': errors.has('email')}"
                             v-model="message.email"
                             placeholder="Your Email">
                      <small class="text-danger" v-if="errors.has('email')">
                        {{ errors.get('email') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-group">
                      <textarea class="form-control" cols="30"
                                name="text"
                                :class="{'is-invalid': errors.has('text')}"
                                v-model="message.text"
                                rows="10" placeholder="Message"></textarea>
                      <small class="text-danger" v-if="errors.has('text')">
                        {{ errors.get('text') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12">
                    <button type="submit" :disabled="errors.any()" class="btn sonar-btn" @click.prevent="sendMessage()">
                      Contact Me
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Api from '@/Api';
import Errors from '@/Errors';

export default {
  data() {
    return {
      message: {
        name: '',
        phone: '',
        email: '',
        text: ''
      },
      errors: new Errors()
    };
  },
  methods: {
    sendMessage() {
      Api.createMessage(this.message)
        .then(() => {
          this.clearForm();
          this.$swal('', 'Сообщение отправлено', 'success');
        })
        .catch(error => {
          this.errors.record(error.response.data);
        });
    },
    clearForm() {
      for (let field in this.message) {
        this.message[field] = '';
      }
      this.errors.clear();
    }
  },
  created() {
    this.$parent.$emit('spinner-state', false);
  },
  mounted() {
    if (this.$route.query.hasOwnProperty('scroll')) {
      this.$scrollTo('#contact-me');
    }
  }
};
</script>
