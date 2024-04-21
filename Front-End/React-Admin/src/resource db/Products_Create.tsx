import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required ,NumberInput,
    ImageInput , ImageField,ReferenceInput} from 'react-admin';

export const ProductCreate = (props:any) => (
<Create>
    <SimpleForm>
        <TextInput source="name" validate={[required()]} />
        <TextInput multiline source="description" validate={[required()]} />
        <NumberInput source="price" validate={[required()]} />
        <ReferenceInput source="category_id" reference='Categories'/>
        <ImageInput source="picture" label="Product Image" accept="image/*">
            <ImageField source="src" title="title" />
        </ImageInput>
    </SimpleForm>
</Create>
)