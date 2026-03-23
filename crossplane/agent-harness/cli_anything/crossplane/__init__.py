import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crossplane running')
@cli.command()
def start(): click.echo('crossplane started')
if __name__ == '__main__': cli()
