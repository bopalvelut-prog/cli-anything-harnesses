import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ingress_nginx running')
@cli.command()
def start(): click.echo('ingress_nginx started')
if __name__ == '__main__': cli()
