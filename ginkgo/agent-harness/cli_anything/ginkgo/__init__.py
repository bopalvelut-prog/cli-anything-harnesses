import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ginkgo running')
@cli.command()
def start(): click.echo('ginkgo started')
if __name__ == '__main__': cli()
