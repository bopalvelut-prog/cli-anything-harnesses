import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Typeform forms')
@cli.command()
def responses(): click.echo('Typeform responses')
if __name__ == '__main__': cli()
