import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('csharp running')
@cli.command()
def start(): click.echo('csharp started')
if __name__ == '__main__': cli()
