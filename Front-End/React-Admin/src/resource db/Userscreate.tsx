import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const UsersCreate = () => (
    <Create>
        <SimpleForm>
            <TextInput source="Name" validate={[required()]} />
            <TextInput source="Password" label="Password" validate={[required()]}/>
            <TextInput source="Email" multiline={true} label="Email" validate={[required()]}/>
            <TextInput source="Phone" multiline={true} label="phone" validate={[required()]}/>
            <DateInput source="registration_date" />
            <TextInput source="Role" />
            <TextInput source="address" multiline={true}/>
        </SimpleForm>
    </Create>
);