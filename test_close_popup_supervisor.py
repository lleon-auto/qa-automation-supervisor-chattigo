from playwright.sync_api import Page, expect

URL = "https://qa-pantera.chattigo.com/login/pages/login"
USER = "supervisor_auto_07_pantera@chattigo.com"
PASSWORD = "Super2024@12."

def test_close_popup(page: Page):
            # 1. Login
            page.goto(URL)
            page.fill('input[formcontrolname="user"]', USER)
            page.fill('input[formcontrolname="password"]', PASSWORD)
            page.click('#loginButton')

            # 2. Detectar y cerrar pop-up
            popup = page.locator(".widget-generic-modal")

            # Hacer clic en el primer botón de cerrar VISIBLE
            page.locator("button.ch-ui-modal__close:visible").first.click()
            print("✅ Pop-up cerrado con botón X")


            # 3. Validar carga del dashboard
            assert page.locator('.c-sidebar-menu__label')
            print("✅ Vista de Supervisor cargada")
