import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sympathy running')
@cli.command()
def start(): click.echo('sympathy started')
if __name__ == '__main__': cli()
