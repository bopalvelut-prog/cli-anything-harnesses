import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('husky running')
@cli.command()
def start(): click.echo('husky started')
if __name__ == '__main__': cli()
