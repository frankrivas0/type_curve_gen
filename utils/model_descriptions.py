
descriptions = {
    'Homogeneous_infinite':  
    
    """
    <h1> <strong> Homogeneous Infinite Model </strong> </h1>
    <p>The Homogeneous Infinite model considers constant wellbore storage and skin factor, 
        in an infinite-homogeneous reservoir with a vertical well.</p>
        <ul>
            <li><strong>Reservoir Model:</strong> Homogeneous </li>
            <li><strong>Boundary Model:</strong> Infinite </li>
            <li><strong>Well Model:</strong> Finite radius </li>
            <li><strong>Wellbore Storage:</strong> Constant </li>
        </ul>

    <h2> Parameters </h2>
        <ul>
            <li><strong>Dimensionless Wellbore Storage Coefficient (CD):</strong> Represents the volume of fluid that can be stored in the wellbore per unit change in pressure. 
                It accounts for the effects of wellbore storage on pressure transient behavior.</li>
            <li><strong>Skin Factor (s):</strong> A dimensionless parameter that quantifies the effect of near-wellbore conditions on fluid flow. 
                A positive skin factor indicates damage or reduced permeability near the wellbore, while a negative skin factor indicates stimulation or enhanced permeability.</li>
        </ul>
        
        """,


    'Homogeneous_Closed_Circular':  
    
    """
    <h1> <strong> Homogeneous Closed Circular Model </strong> </h1>
    <p>The Homogeneous Closed Circular model considers constant wellbore storage and skin factor, 
        in a closed circular homogeneous reservoir with a vertical well. When the pressure disturbance reaches the reservoir boundaries, 
        the flow regime transitions from transient to pseudo-steady state (PSS). During the PSS flow regime, the pressure at any location
        in the reservoir changes linearly as a function of time.</p>
        <ul>
            <li><strong>Reservoir Model:</strong> Homogeneous </li>
            <li><strong>Boundary Model:</strong> Closed Circular </li>
            <li><strong>Well Model:</strong> Finite radius </li>
            <li><strong>Wellbore Storage:</strong> Constant </li>
        </ul>

    <h2> Parameters </h2>
        <ul>
            <li><strong>Dimensionless Wellbore Storage Coefficient (CD):</strong> Represents the volume of fluid that can be stored in the wellbore per unit change in pressure. 
                It accounts for the effects of wellbore storage on pressure transient behavior.</li>
            <li><strong>Skin Factor (s):</strong> A dimensionless parameter that quantifies the effect of near-wellbore conditions on fluid flow. 
                A positive skin factor indicates damage or reduced permeability near the wellbore, while a negative skin factor indicates stimulation or enhanced permeability.</li>
            <li><strong>Dimensionless Reservoir Radius (reD):</strong> Represents the size of the reservoir relative to the wellbore radius. 
                It influences the pressure response as the pressure disturbance reaches the reservoir boundary.</li>   
        </ul>
        
        """,

    'Homogeneous_Constant_Pressure_Circular':  
    
    """
    <h1> <strong> Homogeneous Constant Pressure Circular Model </strong> </h1>
    <p>The Homogeneous Constant Pressure Circular model considers constant wellbore storage and skin factor, 
        in a circular homogeneous reservoir with a vertical well. When the pressure disturbance reaches the reservoir boundaries, 
        the flow regime transitions from transient to steady state. During the steady state flow regime, the pressure at any location
        in the reservoir remains constant with respect to time. This flow regime can occur due to strong aquifer.</p>
        <ul>
            <li><strong>Reservoir Model:</strong> Homogeneous </li>
            <li><strong>Boundary Model:</strong> Constant pressure Circular </li>
            <li><strong>Well Model:</strong> Finite radius </li>
            <li><strong>Wellbore Storage:</strong> Constant </li>
        </ul>

    <h2> Parameters </h2>
        <ul>
            <li><strong>Dimensionless Wellbore Storage Coefficient (CD):</strong> Represents the volume of fluid that can be stored in the wellbore per unit change in pressure. 
                It accounts for the effects of wellbore storage on pressure transient behavior.</li>
            <li><strong>Skin Factor (s):</strong> A dimensionless parameter that quantifies the effect of near-wellbore conditions on fluid flow. 
                A positive skin factor indicates damage or reduced permeability near the wellbore, while a negative skin factor indicates stimulation or enhanced permeability.</li>
            <li><strong>Dimensionless Reservoir Radius (reD):</strong> Represents the size of the reservoir relative to the wellbore radius. 
                It influences the pressure response as the pressure disturbance reaches the reservoir boundary.</li>   
        </ul>
        
        """,


    'Dual_porosity_PSS':
    
    """
    <h1> <strong> Dual porosity PSS Model </strong> </h1>
    <p>The Dual porosity or Naturally fractured PSS reservoir model considers constant wellbore storage and skin factor, 
        in a reservoir with a vertical well. It assumes that the flow between the matrix and fracture systems is pseudo-steady state (PSS).
        At early time, the flow comes from the fluid stored in the fractures. Then there is a interporosity flow transition. It is identified 
        by a dip in the Bourdet derivative. After the interporosity flow, the flow comes from the total system fractures-matrix.</p>
        <ul>
            <li><strong>Reservoir Model:</strong> Dual porosity PSS </li>
            <li><strong>Boundary Model:</strong> Infinite </li>
            <li><strong>Well Model:</strong> Finite radius </li>
            <li><strong>Wellbore Storage:</strong> Constant </li>
        </ul>

    <h2> Parameters </h2>
        <ul>
            <li><strong>Dimensionless Wellbore Storage Coefficient (CD):</strong> Represents the volume of fluid that can be stored in the wellbore per unit change in pressure. 
                It accounts for the effects of wellbore storage on pressure transient behavior.</li>
            <li><strong>Skin Factor (s):</strong> A dimensionless parameter that quantifies the effect of near-wellbore conditions on fluid flow. 
                A positive skin factor indicates damage or reduced permeability near the wellbore, while a negative skin factor indicates stimulation or enhanced permeability.</li>
            <li><strong>Storativity Coefficient (ω):</strong> A dimensionless parameter that represents the percentage of fluid stored in the
            fracture system relative to the total fluid in the reservoir. A storativity coefficient of 1 indicates that all fluid is stored in the fracture system, while a 
            coefficient of 0 indicates that all fluid is stored in the matrix system. The lower the storativity coefficient, the longer it takes
            for the matrix and fracture system to reach a state of equilibrium. It effect on the bourdet derivative is the depht of the dip.</li>
            <li><strong>Interporosity Flow Coefficient (λ):</strong> A dimensionless parameter that is defined as the ratio of the permeability
            of the matrix to the permeability of the fracture system, adjusted by the geometric properties of the matrix blocks. It characterizes
            the ease with which fluid can flow between the matrix and fracture systems. A higher interporosity flow coefficient indicates a greater 
            ability for fluid to transfer between the two systems. It produces a shift in the dip characteristic to dual porosity.</li>
        </ul>
        
        """,


    'Dual_porosity_sphere': 
    
    """
    <h1> <strong> Dual porosity transient sphere </strong> </h1>
    <p>The Dual porosity transient sphere reservoir model considers constant wellbore storage and skin factor, 
        in a reservoir with a vertical well. It assumes that the flow between the matrix and fracture systems is transient (time dependent) 
        and that the matrix blocks are spherical. At early time, the flow comes from the fluid stored in the fractures. Then there is a interporosity flow transition. It is identified 
        by a dip in the Bourdet derivative. After the interporosity flow, the flow comes from the total system fractures-matrix.</p>
        <ul>
            <li><strong>Reservoir Model:</strong> Dual porosity transient sphere </li>
            <li><strong>Boundary Model:</strong> Infinite </li>
            <li><strong>Well Model:</strong> Finite radius </li>
            <li><strong>Wellbore Storage:</strong> Constant </li>
        </ul>

    <h2> Parameters </h2>
        <ul>
            <li><strong>Dimensionless Wellbore Storage Coefficient (CD):</strong> Represents the volume of fluid that can be stored in the wellbore per unit change in pressure. 
                It accounts for the effects of wellbore storage on pressure transient behavior.</li>
            <li><strong>Skin Factor (s):</strong> A dimensionless parameter that quantifies the effect of near-wellbore conditions on fluid flow. 
                A positive skin factor indicates damage or reduced permeability near the wellbore, while a negative skin factor indicates stimulation or enhanced permeability.</li>
            <li><strong>Storativity Coefficient (ω):</strong> A dimensionless parameter that represents the percentage of fluid stored in the
            fracture system relative to the total fluid in the reservoir. A storativity coefficient of 1 indicates that all fluid is stored in the fracture system, while a 
            coefficient of 0 indicates that all fluid is stored in the matrix system. The lower the storativity coefficient, the longer it takes
            for the matrix and fracture system to reach a state of equilibrium.</li>
            <li><strong>Interporosity Flow Coefficient (λ):</strong> A dimensionless parameter that is defined as the ratio of the permeability
            of the matrix to the permeability of the fracture system, adjusted by the geometric properties of the matrix blocks. It characterizes
            the ease with which fluid can flow between the matrix and fracture systems. A higher interporosity flow coefficient indicates a greater 
            ability for fluid to transfer between the two systems.</li>
        </ul>
        
        """,


    'Dual_porosity_slab': 
    
    """
    <h1> <strong> Dual porosity transient slabs </strong> </h1>
    <p>The Dual porosity transient slap reservoir model considers constant wellbore storage and skin factor, 
        in a reservoir with a vertical well. It assumes that the flow between the matrix and fracture systems is transient (time dependent) 
        and that the matrix blocks are slabs. At early time, the flow comes from the fluid stored in the fractures. Then there is a interporosity flow transition. It is identified 
        by a dip in the Bourdet derivative. After the interporosity flow, the flow comes from the total system fractures-matrix.</p>
        <ul>
            <li><strong>Reservoir Model:</strong> Dual porosity transient slabs </li>
            <li><strong>Boundary Model:</strong> Infinite </li>
            <li><strong>Well Model:</strong> Finite radius </li>
            <li><strong>Wellbore Storage:</strong> Constant </li>
        </ul>

    <h2> Parameters </h2>
        <ul>
            <li><strong>Dimensionless Wellbore Storage Coefficient (CD):</strong> Represents the volume of fluid that can be stored in the wellbore per unit change in pressure. 
                It accounts for the effects of wellbore storage on pressure transient behavior.</li>
            <li><strong>Skin Factor (s):</strong> A dimensionless parameter that quantifies the effect of near-wellbore conditions on fluid flow. 
                A positive skin factor indicates damage or reduced permeability near the wellbore, while a negative skin factor indicates stimulation or enhanced permeability.</li>
            <li><strong>Storativity Coefficient (ω):</strong> A dimensionless parameter that represents the percentage of fluid stored in the
            fracture system relative to the total fluid in the reservoir. A storativity coefficient of 1 indicates that all fluid is stored in the fracture system, while a 
            coefficient of 0 indicates that all fluid is stored in the matrix system. The lower the storativity coefficient, the longer it takes
            for the matrix and fracture system to reach a state of equilibrium.</li>
            <li><strong>Interporosity Flow Coefficient (λ):</strong> A dimensionless parameter that is defined as the ratio of the permeability
            of the matrix to the permeability of the fracture system, adjusted by the geometric properties of the matrix blocks. It characterizes
            the ease with which fluid can flow between the matrix and fracture systems. A higher interporosity flow coefficient indicates a greater 
            ability for fluid to transfer between the two systems.</li>
        </ul>
        
        """
    
}