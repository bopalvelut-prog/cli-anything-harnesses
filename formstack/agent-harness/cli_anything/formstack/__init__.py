import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Formstack forms')
@cli.command()
def submissions(): click.echo('Formstack submissions')
if __name__ == '__main__': cli()
