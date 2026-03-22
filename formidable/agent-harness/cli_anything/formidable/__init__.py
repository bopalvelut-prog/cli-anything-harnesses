import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Formidable Forms forms')
@cli.command()
def entries(): click.echo('Formidable Forms entries')
if __name__ == '__main__': cli()
