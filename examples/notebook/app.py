@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = NoteForm()
    note = db.session.get(Note, note_id)
    if form.validate_on_submit():
        note.title = form.title.data
        note.body = form.body.data
        db.session.commit()
        flash('Note updated.')
        return redirect(url_for('index'))
    if request.method == 'GET':
        # pre-fill form
        form.title.data = note.title
        form.body.data = note.body
    return render_template('edit_note.html', form=form)

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = db.session.get(Note, note_id)
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted.')
    else:
        flash('Delete failed, please try again.')
    return redirect(url_for('index'))