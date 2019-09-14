<template>
  <div>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">

      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail equalize bg-img"
           style="background-image: url(/img/bg-img/contact.jpg);"></div>

      <!-- Hero Content -->
      <div id="phone-block" class="hero-content equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-8">
              <div class="line"></div>
              <h2>Контакты</h2>
              <p>{{ phoneNumber }}</p>
              <a href="#" v-scroll-to="'#contact-me'" class="btn sonar-btn white-btn">
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
                             placeholder="Ваше имя">
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
                             placeholder="Номер телефона"
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
                             placeholder="Ваш Email (необязательно)">
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
      phoneNumber: '',
      message: {
        name: '',
        phone: '',
        email: '',
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
            text: 'Мы свяжемся с вами в ближайшее время',
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
          if (!this.isErrorsInFields) {
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
        this.phoneNumber = data.phone_number;
      })
      .then(() => {
        this.$parent.$emit('spinner-state', false);
      });
  },
  mounted() {
    if (this.$route.query.hasOwnProperty('scroll')) {
      this.$scrollTo('#phone-block');
    }
  }
};
</script>
