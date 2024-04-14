import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const ShippingAddresses_Creat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="user_id" validate={[required()]} />
            <TextInput source="recipient_name" multiline={true}/>
            <TextInput source="address_line1"/>
            <TextInput source="address_line2"/>
            <TextInput source="city"/>
            <TextInput source="state"/>
            <TextInput source="postal_code"/>
            <TextInput source="country"/>
        </SimpleForm>
    </Create>
);