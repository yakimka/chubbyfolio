<template>
  <div>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">

      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail equalize bg-img"
           style="background-image: url(/img/bg-img/contact.jpg);"></div>

      <!-- Hero Content -->
      <div id="" class="hero-content phone-block equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-8">
              <div class="line"></div>
              <h2 id="contacts">Контакты</h2>
              <div class="contact-me-social-area" v-if="social">
                <p><span>Город Киев</span></p>
                <p>
                  <a :href="`tel:${social.phone_number}`" data-toggle="tooltip"
                     data-placement="bottom" title="Phone Number" v-if="social.phone_number">
                    <font-awesome-icon :icon="['fa', 'phone']"/>
                    {{ social.phone_number }}
                  </a>
                </p>
                <p>
                  <a :href="social.instagram_link" target="_blank" data-toggle="tooltip"
                     data-placement="bottom" title="Instagram" v-if="social.instagram_link">
                    <font-awesome-icon :icon="['fab', 'instagram']"/>
                    Instagram
                  </a>
                </p>
                <p>
                  <a :href="social.facebook_link" target="_blank" data-toggle="tooltip"
                     data-placement="bottom" title="Facebook" v-if="social.facebook_link">
                    <font-awesome-icon :icon="['fab', 'facebook']"/>
                    Facebook
                  </a>
                </p>
              </div>
              <a href="#" v-scroll-to="'#contact-me'" class="btn sonar-btn white-btn mt-25">
                или напишите мне
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Hero Area End ***** -->

    <section class="sonar-contact-area section-padding-100" id="contact-me">
      <!-- back end content -->
      <div class="backEnd-content">
        <img class="dots" src="/img/core-img/dots.png" alt="">
      </div>

      <div class="container">
        <div class="row">
          <!-- Contact Form Area -->
          <div class="col-12">
            <div class="contact-form text-center bg-white-alpha">

              <h2>Напишите мне и я Вам перезвоню</h2>

              <form id="feedback-form"
                    action="#"
                    method="post"
                    @keydown="errors.clear($event.target.name)">
                <div class="row">
                  <div class="col-12 col-md-6">
                    <div class="form-group">
                      <input type="text" class="form-control"
                             name="name"
                             :class="{'is-invalid': errors.has('name')}"
                             v-model="message.name"
                             placeholder="Ваше имя">
                      <small class="text-danger" v-if="errors.has('name')">
                        {{ errors.get('name') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12 col-md-6">
                    <div class="form-group">
                      <input type="tel" class="form-control"
                             name="phone"
                             :class="{'is-invalid': errors.has('phone')}"
                             v-model="message.phone"
                             placeholder="Номер телефона"
                             v-mask="'+38(###) ###-##-##'">
                      <small class="text-danger" v-if="errors.has('phone')">
                        {{ errors.get('phone') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-group">
                      <textarea class="form-control" cols="30"
                                name="text"
                                :class="{'is-invalid': errors.has('text')}"
                                v-model="message.text"
                                rows="10" placeholder="Текст сообщения (необязательно)"></textarea>
                      <small class="text-danger" v-if="errors.has('text')">
                        {{ errors.get('text') }}
                      </small>
                    </div>
                  </div>
                  <div class="col-12">
                    <button type="submit" :disabled="isErrorsInFields" class="btn sonar-btn"
                            @click.prevent="sendMessage()">
                      отправить
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
import { getSocialInfo } from '@/helpers';

export default {
  data() {
    return {
      social: null,
      message: {
        name: '',
        phone: '',
        text: ''
      },
      errors: new Errors()
    };
  },
  // TODO вынести функционал формы, всплывающих сообщений,
  // обработки ошибок в отдельные функции\классы
  methods: {
    sendMessage() {
      this.errors.clear();
      Api.createMessage(this.message)
        .then(() => {
          this.clearForm();
          this.$swal({
            title: 'Сообщение отправлено',
            text: 'Я перезвоню Вам в ближайшее время',
            type: 'success',
            confirmButtonText: 'На главную'
          })
            .then((result) => {
              if (result.value) {
                this.$router.push({ name: 'home' });
              }
            });
        })
        .catch(error => {
          this.errors.record(error.response.data);
          if (this.isErrorsInFields) {
            this.$scrollTo('#feedback-form');
          } else {
            let errorText = 'Произошла ошибка. Попробуйте позже.';
            if (error.response.status === 429) {
              errorText = 'Вы превысили максимальное количество запросов. Повторите позже.';
            }
            this.$swal({
              title: 'Ой',
              text: errorText,
              type: 'error'
            });
          }
        });
    },
    clearForm() {
      for (let field in this.message) {
        this.message[field] = '';
      }
      this.errors.clear();
    }
  },
  computed: {
    isErrorsInFields() {
      return this.errors.any(Object.keys(this.message));
    }
  },
  created() {
    getSocialInfo()
      .then(data => {
        this.social = data;
      })
      .then(() => {
        this.$parent.$emit('spinner-state', false);
      });
  },
  mounted() {
    if (this.$route.query.hasOwnProperty('scroll')) {
      this.$scrollTo('#contacts');
    }
  }
};
</script>
