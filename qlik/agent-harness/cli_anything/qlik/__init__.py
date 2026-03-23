import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('qlik running')
@cli.command()
def start(): click.echo('qlik started')
if __name__ == '__main__': cli()
