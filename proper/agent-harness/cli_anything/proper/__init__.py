import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('proper running')
@cli.command()
def start(): click.echo('proper started')
if __name__ == '__main__': cli()
