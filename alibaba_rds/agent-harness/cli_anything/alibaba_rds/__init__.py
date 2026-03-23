import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('alibaba_rds running')
@cli.command()
def start(): click.echo('alibaba_rds started')
if __name__ == '__main__': cli()
