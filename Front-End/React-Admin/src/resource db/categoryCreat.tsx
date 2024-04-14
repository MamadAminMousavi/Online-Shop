import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ReferenceInput } from 'react-admin';

export const CategoryCreat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="name" validate={[required()]} />
            <TextInput source="description" multiline={true}/>
            <ReferenceInput source="parent_category_id" reference='Categories'/>
        </SimpleForm>
    </Create>
);