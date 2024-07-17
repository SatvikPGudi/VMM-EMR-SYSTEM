const Footer_component = () => {
    return (
    <footer className="footer footer-center bg-base-300 text-base-content text-center p-10">
        <aside className="pt-4"> {/* Adjust 'pt-4' to whatever padding you need */}
            <p>Copyright © {new Date().getFullYear()} - All rights reserved by Virtual Medical Missions</p>
        </aside>
    </footer>
    )
}

export default Footer_component
