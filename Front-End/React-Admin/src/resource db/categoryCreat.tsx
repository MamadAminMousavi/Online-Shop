import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const CategoryCreat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="name" validate={[required()]} />
            <TextInput source="description" multiline={true}/>
            <TextInput source="parent_category_id"/>
        </SimpleForm>
    </Create>
);