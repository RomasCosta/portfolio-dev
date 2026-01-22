
        // Criar partículas animadas
        function createParticles() {
            const particlesContainer = document.getElementById('particles');
            const particleCount = 50;

            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                
                const size = Math.random() * 4 + 2;
                particle.style.width = size + 'px';
                particle.style.height = size + 'px';
                
                particle.style.left = Math.random() * 100 + '%';
                
                const duration = Math.random() * 3 + 4;
                particle.style.animationDuration = duration + 's';
                
                const delay = Math.random() * 6;
                particle.style.animationDelay = delay + 's';
                
                particlesContainer.appendChild(particle);
            }
        }

        // Funções para editar descrição (somente front-end)
        function toggleEdit() {
            document.getElementById('description-text').style.display = 'none';
            document.getElementById('edit-form').style.display = 'block';
            document.querySelector('.edit-btn').style.display = 'none';
        }

        function cancelEdit() {
            document.getElementById('description-text').style.display = 'block';
            document.getElementById('edit-form').style.display = 'none';
            document.querySelector('.edit-btn').style.display = 'inline-block';
        }

        function saveDescription() {
            const desc = document.getElementById('description-input').value;
            document.getElementById('description-text').textContent = desc;
            cancelEdit();
        }

        document.addEventListener('DOMContentLoaded', createParticles);