import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bpftrace running')
@cli.command()
def start(): click.echo('bpftrace started')
if __name__ == '__main__': cli()
