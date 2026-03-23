import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Glitch start')
@cli.command()
def remix(): click.echo('Glitch remix')
if __name__ == '__main__': cli()
