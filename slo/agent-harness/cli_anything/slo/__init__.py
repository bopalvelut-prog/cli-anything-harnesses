import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slo running')
@cli.command()
def start(): click.echo('slo started')
if __name__ == '__main__': cli()
