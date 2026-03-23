import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clerk running')
@cli.command()
def start(): click.echo('clerk started')
if __name__ == '__main__': cli()
