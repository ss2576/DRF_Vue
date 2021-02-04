<template lang="pug">
  form.form-horizontal(@submit="submitForm")
    .form-group
      .col-1
         label.form-label.float-right Начало
      .col-1
      .col-3
        input.form-input(type="datetime-local" v-model="for_day")
      .col-3
        label.form-label.float-right Окончания
      .col-1
      .col-3
        input.form-input(type="datetime-local" v-model="to_day")
    .form-group
      .col-1
         label.form-label.float-right Заголовок
      .col-1
      .col-10
         input.form-input(type="text" v-model="title" placeholder="Введите название предстоящего события...")
    .form-group
      .col-1
         label.form-label.float-right Текст
      .col-1
      .col-10
         textarea.form-input(v-model="body" rows=8 placeholder="Введите описание предстоящего события...")
    .form-group
      .col-2
      .col-10
         button.btn.btn-primary.float-right(type="submit") Сохранить
</template>

<script>
export default {
  name: 'create-note',
  data () {
    return {
      'title': '',
      'body': '',
      'for_day': '',
      'to_day': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createNote()
      this.title = ''
      this.body = ''
      this.for_day = ''
      this.to_day = ''
      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', {
        title: this.title, body: this.body, for_day: this.for_day, to_day: this.to_day
      })
    }
  }
}
</script>

<style>
</style>
