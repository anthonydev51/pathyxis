<template>
  <main class="container">
    <header style="text-align: center; margin-top: 2rem;">
      <img src="/logo.png" alt="Pathyxis Logo" style="width: 80px;" />
      <h1>Pathyxis</h1>
      <p>Malware File Scanner using VirusTotal</p>
    </header>

    <section style="margin-top: 3rem;">
      <form @submit.prevent="handleScan">
        <label for="file">Choose a file to scan:</label>
        <input type="file" id="file" @change="onFileChange" />

        <button type="submit" :disabled="!file">Scan File</button>
      </form>
    </section>

    <section v-if="status || result" style="margin-top: 2rem;">
      <article>
        <h4>Status</h4>
        <p v-if="status">{{ status }}</p>

        <div v-if="result">
          <h4>Scan Result</h4>
          <ul>
            <li><strong>File name:</strong> {{ result.fileName }}</li>
            <li><strong>Detection count:</strong> {{ result.detections }}/70</li>
            <li><strong>Scan ID:</strong> {{ result.scanId }}</li>
          </ul>
        </div>
      </article>
    </section>
  </main>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      status: '',
      result: null,
    }
  },
  methods: {
    onFileChange(event) {
      this.file = event.target.files[0]
      this.status = ''
      this.result = null
    },
    async handleScan() {
      if (!this.file) return

      this.status = 'Uploading and scanning...'
      this.result = null

      try {
        const formData = new FormData()
        formData.append('file', this.file)

        const response = await fetch('http://localhost:5000/scan', {
          method: 'POST',
          body: formData,
        })

        if (!response.ok) {
          const errorData = await response.json()
          this.status = `Error: ${errorData.error || response.statusText}`
          return
        }

        const data = await response.json()

        this.status = 'Scan complete!'
        this.result = {
          fileName: data.fileName,
          detections: data.detections,
          scanId: data.scanId,
        }
      } catch (error) {
        this.status = 'Error: ' + error.message
      }
    },
  },
}
</script>

<style>
body {
  background-color: #121212;
  color: #e0e0e0;
  font-family: system-ui, sans-serif;
}

main.container {
  min-height: 100vh;
  padding: 2rem;
}

input[type="file"],
button {
  background-color: #1f1f1f;
  color: #e0e0e0;
  border: 1px solid #444;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  margin-top: 0.5rem;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

h1,
h4,
p,
label {
  color: #e0e0e0;
}
</style>